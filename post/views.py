'''
views - файл, в котором мы будем помещать "представления" нашего приложения.

FBV (function-based views) - представления, основанные на функциях.
CBV (class-based views) - представления, основанные на классах.

http - протокол передачи гипертекста.
request - объект, который содержит информацию о запросе.

Method - метод, который был использован для отправки запроса.
GET - получение данных.
POST - отправка данных.
PUT - обновление данных.
DELETE - удаление данных.

response - объект, который содержит информацию о том, что будет возвращено пользователю.
status code - код состояния, который будет возвращен пользователю.
200 - OK.
404 - Not Found.
500 - Internal Server Error.

render - функция, которая отображает шаблон и возвращает ответ.
'''

from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world!")


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
