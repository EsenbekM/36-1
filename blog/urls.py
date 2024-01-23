from django.contrib import admin
from django.urls import path
from post.views import hello_view, main_page_view, \
    post_list_view, post_detail_view, hashtags_list_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_page_view),
    path('hello/', hello_view),
    path('posts/', post_list_view),
    path('posts/<int:post_id>/', post_detail_view),

    path('hashtags/', hashtags_list_view),
]
