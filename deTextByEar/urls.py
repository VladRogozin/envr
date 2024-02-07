from django.urls import path
from .views import *


urlpatterns = [
    path('show_data/', show_random_word, name='show_data'),
    path('playlist/<int:playlist_id>/', random_word_from_playlist, name='random_word_from_playlist'),
    path('textByEar/<int:amount>/', DeTextByEarListView.as_view(), name='textByEar-list'),
    path('textByEar/create/', DeTextByEarCreateView.as_view(), name='textByEar-create'),
]