from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegistrationView, LogoutView, UserDeleteView

app_name = "accounts"
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", UserRegistrationView.as_view(), name="user_register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete/", UserDeleteView.as_view(), name="user_delete"),
]
