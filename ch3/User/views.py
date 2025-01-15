from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = {"username", "email", "bio"}


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("User:home")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "User/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("User:home")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("User:home")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "User/signup.html", context)


def home(request):
    return render(request, "User/home.html")


def user_profile(request, username):
    user = get_object_or_404(models.CustomUser, username=username)
    return render(request, "User/user_profile.html", {"user_profile": user})
