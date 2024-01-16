from django.contrib import admin
from django.urls import path
from post.views import hello_view, main_page_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_page_view),
    path('hello/', hello_view)
]
