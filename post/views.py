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

QuerySet - набор объектов, полученных в результате запроса к базе данных.

'''

from django.shortcuts import render
from django.http import HttpResponse

from post.models import HashTag, Post, Comment


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world!")


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def post_list_view(request):
    if request.method == 'GET':
        # 1 - получить все посты
        posts = Post.objects.all() # QuerySet

        # 2 - передать их в шаблон
        context = {'posts': posts}

        # 3 - отобразить шаблон
        return render(
            request, 
            'post/list.html',
            context=context
            )
    

def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id) # Post
        except Post.DoesNotExist:
            return render(
                request,
                'errors/404.html',
            )

        return render(
            request,
            'post/detail.html',
            context={'post': post}
        )

# comment.post - объект поста
# post.comments - QuerySet всех комментариев поста


def hashtags_list_view(request):
    if request.method == 'GET':
        hashtags = HashTag.objects.all()

        return render(
            request,
            'hashtags/list.html',
            {"hashtags": hashtags}
        )