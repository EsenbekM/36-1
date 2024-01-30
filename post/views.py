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

from django.shortcuts import render, redirect
from django.http import HttpResponse

from post.models import HashTag, Post, Comment
from post.forms import PostCreateForm, PostCreateForm2, CommentCreateForm


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
        form = CommentCreateForm()
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
            context={'post': post, 'comment_form': form}
        )
    
def comment_create_view(request, post_id):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.save()

        return redirect('post_detail', post_id=post_id)

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
    

def post_create_view(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm2()
        }

        return render(
            request,
            'post/create.html',
            context=context
        )

    elif request.method == 'POST':
        form = PostCreateForm2(request.POST, request.FILES)

        if form.is_valid():
            # Post.objects.create(**form.cleaned_data)
            form.save()
            return redirect('posts_list')

        context = {
            'form': form
        }

        return render(
            request,
            'post/create.html',
            context=context
        )
