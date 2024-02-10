from django.urls import path
from post.views import hello_view, main_page_view, post_list_view, post_detail_view, hashtags_list_view, \
    post_create_view, comment_create_view, post_update_view, PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('', main_page_view),
    path('hello/', hello_view),
    # path('hello2/', HelloView.as_view()), # as_view() - метод класса нужен для того, чтобы Django мог создать экземпляр класса и вызвать метод dispatch()
    path('posts/', post_list_view, name='posts_list'),
    path('posts2/', PostListView.as_view(), name='posts_list2'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/update/', post_update_view, name='post_update'),
    path('posts/create/', PostCreateView.as_view()),
    # path('posts/create2/', PostCreateView.as_view(), name='post_create2'),
    path('posts/<int:post_id>/comment/', comment_create_view, name='comment_create'),
    path('hashtags/', hashtags_list_view),
]