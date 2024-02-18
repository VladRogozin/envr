from .models import VerbWord
from random import sample
import json
import g4f

from django.http import JsonResponse
from django.shortcuts import render


def word_list(request):
    words = VerbWord.objects.all()
    random_words = sample(list(words), 10)
    return render(request, 'deVerbs/play_list.html', {'random_words': random_words})


def check_and_trim_result(result):
    # Замена символов ** и * на двойные и одинарные кавычки
    result = result.replace('**', '"')
    result = result.replace('*', "'")

    # Проверка на наличие "Source:" или "Источник:" и обрезка строки результата
    source_index = result.find('Source:')
    if source_index != -1:
        result = result[:source_index]
    source_index_russian = result.find('Источник:')
    if source_index_russian != -1:
        result = result[:source_index_russian]
    return result

def help_check(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        user_message = body_data.get('user_message')
        result = check_post(user_message, 'help')
        result = check_and_trim_result(result)
        response_data = {
            'user_message': result,
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method'})


def example_check(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        user_message = body_data.get('user_message')
        result = check_post(user_message, "example")
        result = check_and_trim_result(result)
        response_data = {
            'user_message': result,
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request method'})


def check_post(message, mean):
    if mean == "example":
        trry = f"Приведи простой пример употребления слова '{message}' на немецком. В ответе только пример на немецком и к нему перевод"
    else:
        trry = f"Что ты можешь рассказать про это слово: '{message}'.Ответ на русском"
    print(trry)
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": trry}],
        stream=True,
    )
    answer = ''
    for message in response:
        answer += message




    return answer