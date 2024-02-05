import json
import g4f
from django.contrib.sites import requests
import requests as python_requests
from django.http import JsonResponse

from django.shortcuts import render
from rest_framework import generics
from .models import DeMessagesReply
from .serializers import DeMessagesReplySerializer


class DeMessagesReplyListView(generics.ListAPIView):
    serializer_class = DeMessagesReplySerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = DeMessagesReply.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class DeMessagesReplyCreateView(generics.CreateAPIView):
    queryset = DeMessagesReply.objects.all()
    serializer_class = DeMessagesReplySerializer



def display_message(request):
    # Получаем одно случайное сообщение из базы
    random_message = DeMessagesReply.objects.order_by('?').first()

    # Передаем сообщение в шаблон
    context = {'message': random_message}
    return render(request, 'deMessagesReply/messag.html', context)


def check_grammar_view(request):
    if request.method == 'POST':
        # Получаем тело запроса
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        user_message = body_data.get('user_message')
        result = check_grammar_languagetool(user_message)

        # Добавляем координаты ошибок к результату
        response_data = {
            'user_message': user_message,
        }
        print(response_data)
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method'})


def check_grammar_languagetool(message):
    trry = f"Correct the grammatical errors in the following German sentence: '{message}' Return the corrected sentence without any further comments or text."

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": trry}],
        stream=True,
    )
    answer = ''
    for message in response:
        answer += message

    return answer























#
# def display_message(request):
#     # Получаем одно случайное сообщение из базы
#     random_message = DeMessagesReply.objects.order_by('?').first()
#
#     # Передаем сообщение в шаблон
#     context = {'message': random_message}
#     return render(request, 'deMessagesReply/messag.html', context)
#
#
# def check_grammar_view(request):
#     if request.method == 'POST':
#         # Получаем тело запроса
#         body_unicode = request.body.decode('utf-8')
#         body_data = json.loads(body_unicode)
#
#         user_message = body_data.get('user_message')
#         result = check_grammar_languagetool(user_message)
#
#         # Добавляем координаты ошибок к результату
#         response_data = {
#             'user_message': user_message,
#             'is_grammar_correct': result['is_grammar_correct'],
#             'error_positions': result['error_positions'],
#         }
#
#         return JsonResponse(response_data)
#
#     return JsonResponse({'error': 'Invalid request method'})
#
#
# def check_grammar_languagetool(message):
#     url = 'https://api.languagetool.org/v2/check'
#     data = {'language': 'de-DE', 'text': message, 'enabledCategories': 'ALL'}
#     response = python_requests.post(url, data=data)
#     result = response.json()
#
#     print(result)
#
#     # Проверяем, есть ли поле 'matches' в результате
#     if 'matches' in result:
#         is_grammar_correct = len(result['matches']) == 0
#         error_positions = [(match['offset'], match['offset'] + match['length']) for match in result['matches']]
#     else:
#         # Если нет ошибок, устанавливаем соответствующие значения
#         is_grammar_correct = True
#         error_positions = []
#
#     return {
#         'is_grammar_correct': is_grammar_correct,
#         'error_positions': error_positions,
#     }

