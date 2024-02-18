from django.urls import path
from .views import *


urlpatterns = [
    path('words/', word_list, name='verb_list'),
    path('check_grammar/', help_check, name='check_grammar_view'),
    path('example_post/', example_check, name='example_post_view'),
]
