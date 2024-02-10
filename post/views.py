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

CRUD - Create, Read, Update, Delete.
DRY - Don't Repeat Yourself.

FBV 
+ Простота, гибкость, явный поток управления, подходит для уникальной логики.
- Трудно расширять, дублирование кода.

CBV
+ Простота расширения, гибкость, меньше дублирования кода.
- Сложность, неявный поток управления, подходит для общей логики.
'''

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from post.models import HashTag, Post, Comment
from post.forms import PostCreateForm, PostCreateForm2, CommentCreateForm


class PostListView(ListView):
    # template_name = 'post/list.html' # default: <app_label>/<model_name>_list.html
    model = Post
    context_object_name = 'posts' # default: object_list

    # context = {'posts': posts}
    
    # Variant 2
    def get_context_data(self):
        context = super().get_context_data() # {'posts': posts}
        context['hashtags'] = HashTag.objects.all() # {'posts': posts, 'hashtags': hashtags}
        
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(user=self.request.user)

        search = self.request.GET.get('search', '')
        hastag = self.request.GET.get('hashtag', '')

        if search:
            queryset = queryset.filter(
                Q(title__contains=search) | 
                Q(content__contains=search)
            )

        if hastag:
            queryset = queryset.filter(hashtags__id=hastag)

        return queryset


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post' # default: object
    template_name = 'post/detail.html' # default: <app_label>/<model_name>_detail.html
    pk_url_kwarg = 'post_id' # default: pk

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentCreateForm()
        context['has_change_permission'] = (context['post'].user == self.request.user)
        return context


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostCreateForm2
    template_name = 'post/create.html' # default: <app_label>/<model_name>_form.html
    success_url = '/posts/'

    def get_absolute_url(self):
        if self.request.user.is_authenticated:
            return reverse('posts_list')
        return reverse('login')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm2
    template_name = 'post/update.html'
    pk_url_kwarg = 'post_id'
    success_url = '/posts/'
    
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if post.user != request.user:
            return HttpResponse('Permission denied', status=403)
        return super().get(request, *args, **kwargs)


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world!")


class HelloView(View):
    def get(self, request):
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
        posts = Post.objects.all()
        # request.user - объект пользователя, который отправил запрос | AnonymousUser
        if request.user.is_authenticated:
            posts.exclude(user=request.user)

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
            'post/post_list.html',
            context=context
            )


# class BaseListView(View):
#     template_name = None
#     model = None
#     form = None

#     def get(self, request):
#         objects = self.model.objects.all()
#         return render(
#             request,
#             self.template_name,
#             {'posts': objects, 'form': self.form}
#         )


# class PostListView(BaseListView):
#     template_name = 'post/list.html'
#     model = Post
#     form = PostCreateForm


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


# class PostDetailView(View):
#     def get(self, request, post_id):
#         form = CommentCreateForm()
#         try:
#             post = Post.objects.get(id=post_id) # Post
#         except Post.DoesNotExist:
#             return render(
#                 request,
#                 'errors/404.html',
#             )
        
#         has_change_permission = (post.user == request.user)

#         context = {'post': post, 'comment_form': form, 'has_change_permission': has_change_permission}

#         return render(
#             request,
#             'post/detail.html',
#             context=context
#         )


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


# class PostCreateView(View):
#     template_name = 'post/create.html'
#     form = PostCreateForm2
#     model = Post

#     def get(self, request):
#         return render(
#             request,
#             self.template_name,
#             context={'form': self.form()}
#         )
    
#     def post(self, request):
#         form = self.form(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')

#         return render(
#             request,
#             self.template_name,
#             context={'form': form}
#         )


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