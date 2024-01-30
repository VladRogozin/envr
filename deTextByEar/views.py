from django.shortcuts import render
from rest_framework import generics
from .models import DeTextByEar
from .serializers import DeTextByEarSerializer


class DeTextByEarListView(generics.ListAPIView):
    serializer_class = DeTextByEarSerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = DeTextByEar.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class DeTextByEarCreateView(generics.CreateAPIView):
    queryset = DeTextByEar.objects.all()
    serializer_class = DeTextByEarSerializer


def show_random_word(request):
    data = DeTextByEar.objects.all()
    random_item = data.order_by('?').first()  # Выбор случайного элемента

    return render(request, 'deTextByEar/random_list.html', {'random_item': random_item})

