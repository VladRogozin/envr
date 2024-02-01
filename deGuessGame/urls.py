from django.urls import path
from .views import *


urlpatterns = [
    path('word/<str:level>/<int:amount>/', DeWordListView.as_view(), name='de-word-list'),
    path('word/create/', DeWordCreateView.as_view(), name='de-word-create'),
    path('random_word/', random_word, name='random_word'),
]