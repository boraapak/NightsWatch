from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        next_page = request.POST['next']
        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)
            if next_page:
                return redirect(next_page)
            return redirect('movie_list')
        return redirect(reverse('login') + "?next=" + next_page)
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        next_page = request.POST['next']
        user = User.objects.create_user(username, password=password)
        user.save()
        django_login(request, user)
        if next_page:
            return redirect(next_page)
        return redirect('movie_list')
    return render(request, 'register.html')


def logout(request):
    next_page = request.GET['next'] if "next" in request.GET else "/"
    django_logout(request)
    return redirect(next_page)
