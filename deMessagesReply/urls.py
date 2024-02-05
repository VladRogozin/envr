from django.urls import path
from .views import *


urlpatterns = [
    path('message/<int:amount>/', DeMessagesReplyListView.as_view(), name='message-list'),
    path('message/create/', DeMessagesReplyCreateView.as_view(), name='message-create'),
    path('check_grammar/', check_grammar_view, name='check_grammar_view'),

    path('message', display_message, name='message'),

]