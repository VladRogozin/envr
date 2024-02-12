import random

from django.shortcuts import render
from rest_framework import generics
from .models import DeTextByEar, Playlist
from .serializers import DeTextByEarSerializer
from django.views.generic import ListView

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

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'deTextByEar/playlist_list.html'
    context_object_name = 'playlists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playlists = Playlist.objects.all()
        random_data = []
        for playlist in playlists:
            # Получаем все объекты DeTextByEar для данного плейлиста
            de_texts = playlist.audios.all()
            # Выбираем случайный объект DeTextByEar
            random_de_text = random.choice(de_texts)
            # Добавляем кортеж в список с плейлистом и случайным объектом DeTextByEar
            random_data.append((playlist, random_de_text))
        context['random_data'] = random_data
        return context

def show_random_word(request):
    data = DeTextByEar.objects.all()
    random_item = data.order_by('?').first()
    playlists = Playlist.objects.all()  # Получите список всех плейлистов
    return render(request, 'deTextByEar/random_list.html', {'random_item': random_item, 'playlists': playlists})


def random_word_from_playlist(request, playlist_id):
    # Получите случайные слова из выбранного плейлиста
    playlist = Playlist.objects.get(pk=playlist_id)
    random_item = playlist.audios.order_by('?').first()  # Получаем случайное слово из плейлиста
    return render(request, 'deTextByEar/random_list.html', {'random_item': random_item, 'playlist': playlist})
