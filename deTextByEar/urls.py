from django.urls import path
from .views import *

urlpatterns = [
    path('show_data/', show_random_word, name='show_data'),
    path('playlists/', PlaylistListView.as_view(), name='playlist_list'),
    path('playlist/<int:playlist_id>/', random_word_from_playlist, name='random_word_from_playlist'),
    path('textByEar/<int:amount>/', DeTextByEarListView.as_view(), name='textByEar-list'),
    path('textByEar/create/', DeTextByEarCreateView.as_view(), name='textByEar-create'),
    path('favorites/', favorite_list, name='favorites'),
    path('add_to_favorites/<int:detext_id>/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:favorite_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('random_word_from_favorites/', random_word_from_favorites, name='random_word_from_favorites'),

]