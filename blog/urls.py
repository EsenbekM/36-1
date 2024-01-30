from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from post.views import hello_view, main_page_view, \
    post_list_view, post_detail_view, hashtags_list_view, post_create_view, comment_create_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_page_view),
    path('hello/', hello_view),
    path('posts/', post_list_view, name='posts_list'),
    path('posts/<int:post_id>/', post_detail_view, name='post_detail'),
    path('posts/create/', post_create_view),
    path('posts/<int:post_id>/comment/', comment_create_view, name='comment_create'),

    path('hashtags/', hashtags_list_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
