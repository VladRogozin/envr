from django.urls import path
from .views import *


urlpatterns = [
    path('spell/<int:amount>/', SpellListView.as_view(), name='spell-list'),
    path('spell/create/', SpellCreateView.as_view(), name='spell-create'),
]