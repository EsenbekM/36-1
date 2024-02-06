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

QueryParameter - параметр запроса, который передается в URL.
Пример: https://example.com/?page=2&limit=10
?v=fd1pYQcu5kA
https://rezka.ag/cartoons/?filter=popular
rezka.ag/cartoons?page=4
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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
        # request.GET - {'search': 'python'}
        search = request.GET.get('search', '')
        sort = request.GET.get('sort', 'created_at')
        hastag = request.GET.get('hashtag', '')
        page = request.GET.get('page', 1)

        # 1 - получить все посты
        posts = Post.objects.all().exclude(user=request.user)

        if search:
            # posts = posts.filter(title__contains=search) | posts.filter(content__contains=search)
            # if search.startswith('#'):
            #     search = search[1:]
            #     posts = posts.filter(
            #         Q(title__contains=search) | 
            #         Q(content__contains=search) |
            #         Q(hashtags__name__contains=search)
            #     )
            posts = posts.filter(
                Q(title__contains=search) | 
                Q(content__contains=search)
            )
        if sort:
            posts = posts.order_by(sort)

        if hastag:
            posts = posts.filter(hashtags__id=hastag)


        limit = 3
        max_pages = posts.__len__() / limit
        if round(max_pages) < max_pages: # 3 < 3.3333... = 4 
            max_pages = round(max_pages) + 1
        else: # 12 < 12.0 = 12
            max_pages = round(max_pages)

        # posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]
        # page = 1, limit = 3
            
        # Formula:
        # start = (page - 1) * limit
        # end = start + limit
        
        start = (int(page) - 1) * limit
        end = start + limit

        posts = posts[start:end]

        # Example 1:
        # page = 1, limit = 3
        # start = (1 - 1) * 3 = 0
        # end = 0 + 3 = 3
            
        # Example 2:
        # page = 2, limit = 3
        # start = (2 - 1) * 3 = 3
        # end = 3 + 3 = 6

        hashtags = HashTag.objects.all()
        context = {'posts': posts, 'hashtags': hashtags, 'max_pages': range(1, max_pages + 1)}

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
        
        has_change_permission = (post.user == request.user)

        context = {'post': post, 'comment_form': form, 'has_change_permission': has_change_permission}

        return render(
            request,
            'post/detail.html',
            context=context
        )
    
@login_required
def comment_create_view(request, post_id):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.user = request.user
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


@login_required
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


@login_required
def post_update_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(
            request,
            'errors/404.html',
        )
    
    if post.user != request.user:
        return HttpResponse('Permission denied', status=403)

    if request.method == 'GET':
        form = PostCreateForm2(instance=post)
        return render(
            request,
            'post/update.html',
            {'form': form}
        )
    
    elif request.method == 'POST':
        form = PostCreateForm2(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post_id)
        return render(
            request,
            'post/update.html',
            {'form': form}
        )

# @login_required
# def post_delete_view(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         return render(
#             request,
#             'errors/404.html',
#         )
    
#     if post.user != request.user:
#         return HttpResponse('Permission denied', status=403)

#     post.delete()
#     return redirect('posts_list')