from django.urls import path
from .views import *


urlpatterns = [
    path('audioStory/<int:amount>/', DeAudioStoryListView.as_view(), name='audioStory-list'),
    path('audioStory/create/', DeAudioStoryCreateView.as_view(), name='audioStory-create'),
]