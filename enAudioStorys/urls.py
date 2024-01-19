from django.urls import path
from .views import *


urlpatterns = [
    path('audioStory/<int:amount>/', EnAudioStoryListView.as_view(), name='audioStory-list'),
    path('audioStory/create/', EnAudioStoryCreateView.as_view(), name='audioStory-create'),
]