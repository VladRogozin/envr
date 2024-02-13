import random
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import DeTextByEar, Playlist, UserSaveDeTextByEar
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

@login_required
def random_word_from_playlist(request, playlist_id):
    # Получите случайные слова из выбранного плейлиста
    playlist = Playlist.objects.get(pk=playlist_id)
    random_item = playlist.audios.order_by('?').first()  # Получаем случайное слово из плейлиста
    return render(request, 'deTextByEar/random_list.html', {'random_item': random_item, 'playlist': playlist})

@login_required
def favorite_list(request):
    favorites = UserSaveDeTextByEar.objects.filter(user=request.user)
    return render(request, 'deTextByEar/favorite_list.html', {'favorites': favorites})


@login_required
def random_word_from_favorites(request):
    favorites = UserSaveDeTextByEar.objects.filter(user=request.user)
    if favorites.exists():
        random_item = favorites.order_by('?').first().detext_by_ear
        return render(request, 'deTextByEar/random_list.html', {'random_item': random_item})
    else:
        return render(request, 'deTextByEar/no_favorites.html')


@login_required
def add_to_favorites(request, detext_id):
    try:
        detext = DeTextByEar.objects.get(pk=detext_id)
        if UserSaveDeTextByEar.objects.filter(user=request.user, detext_by_ear=detext).exists():
            response_data = {'success': False, 'message': 'Bже додано в обране.'}
        else:
            favorite_detext = UserSaveDeTextByEar(user=request.user, detext_by_ear=detext)
            favorite_detext.save()
            response_data = {'success': True, 'message': 'Успішно додано в обране.'}
    except DeTextByEar.DoesNotExist:
        response_data = {'success': False, 'message': 'Детекст не знайдено'}
    except Exception as e:
        response_data = {'success': False, 'message': f'Помилка під час додавання детексту в обране: {str(e)}'}

    return JsonResponse(response_data)

@login_required
def remove_from_favorites(request, favorite_id):
    favorite_detext = UserSaveDeTextByEar.objects.get(pk=favorite_id)
    favorite_detext.delete()
    return redirect('favorites')




def render_game_page(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    audios = [{'audio': audio.audio.url, 'text': audio.text} for audio in playlist.audios.all()]
    context = {
        'playlist': audios,
        'playlistName': playlist.name,
    }

    print(audios)
    return render(request, 'deTextByEar/start_test.html', context)
