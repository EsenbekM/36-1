import random

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from user.forms import RegisterForm, LoginForm, VeryfyForm
from user.models import Profile, SMSCodes


def register_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html', {'form': RegisterForm()})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            avatar = form.cleaned_data['avatar']
            bio = form.cleaned_data['bio']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_active=False
            )
            Profile.objects.create(
                user=user,
                avatar=avatar,
                bio=bio,
            )
            code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
            SMSCodes.objects.create(
                user=user,
                code=code
            )
            # TODO: отправить код на почту

            return redirect('veryfy')
        else:
            return render(request, 'user/register.html', {'form': form})


def veryfy_view(request):
    if request.method == 'GET':
        return render(request, 'user/veryfy.html', {'form': VeryfyForm()})
    elif request.method == 'POST':
        form = VeryfyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if SMSCodes.objects.filter(code=code).exists():
                sms_code = SMSCodes.objects.get(code=code)
                sms_code.user.is_active = True
                sms_code.user.save()
                sms_code.delete()
                return redirect('login')
            else:
                form.add_error(None, 'Invalid code')
                return render(request, 'user/veryfy.html', {'form': form})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', {'form': LoginForm()})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data) # None or User object

            if user is not None:
                login(request, user) # запишет в сессию пользователя
                return redirect('posts_list')
            else:
                form.add_error(None, 'Invalid credentials')
                return render(request, 'user/login.html', {'form': form})


def profile_view(request):
    return render(request, 'user/profile.html')


def logout_view(request):
    logout(request)
    return redirect('posts_list')