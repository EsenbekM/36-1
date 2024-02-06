from django.urls import path
from post.views import hello_view, main_page_view, post_list_view, post_detail_view, hashtags_list_view, post_create_view, comment_create_view, post_update_view


urlpatterns = [
    path('', main_page_view),
    path('hello/', hello_view),
    path('posts/', post_list_view, name='posts_list'),
    path('posts/<int:post_id>/', post_detail_view, name='post_detail'),
    path('posts/<int:post_id>/update/', post_update_view, name='post_update'),
    path('posts/create/', post_create_view),
    path('posts/<int:post_id>/comment/', comment_create_view, name='comment_create'),
    path('hashtags/', hashtags_list_view),
]