from django.urls import path

from user.views import register_view, login_view, \
    profile_view, logout_view, veryfy_view, profile_update_view


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('verify/', veryfy_view, name='veryfy'),
    path('profile/update/', profile_update_view, name='profile_update'),
]
