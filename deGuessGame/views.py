import random

from django.shortcuts import render
from rest_framework import generics
from .models import DeWord
from .serializers import DeWordSerializer
from django.http import JsonResponse


class DeWordListView(generics.ListAPIView):
    serializer_class = DeWordSerializer

    def get_queryset(self):
        level = self.kwargs.get('level', None)
        amount = self.kwargs.get('amount', 10)

        queryset = DeWord.objects.all()

        if level and level != 'None':
            queryset = queryset.filter(word_level=level)

        if not queryset.exists():
            # Если нет данных, возвращаем JSON-ответ с информацией
            return JsonResponse({"detail": "No matching data found"}, status=404)

        queryset = queryset.order_by('?')

        return queryset[:amount]


class DeWordCreateView(generics.CreateAPIView):
    queryset = DeWord.objects.all()
    serializer_class = DeWordSerializer


def random_word(request):
    # Получаем случайное слово из базы данных
    random_de_word = DeWord.objects.order_by('?').first()

    # Получаем случайное вспомогательное слово для выбранного слова
    auxiliary_words = random_de_word.auxiliary_words
    random_auxiliary_word = dict(auxiliary_words)
    context = {
        'original_word': random_de_word.original_word,
        'translated_word': random_de_word.translated_word,
        'auxiliary_word': random_auxiliary_word,
    }

    return render(request, 'deGuessGame/show.html', context)
