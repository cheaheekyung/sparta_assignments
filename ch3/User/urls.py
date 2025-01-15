from django.urls import path
from . import views

app_name = "User"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("", views.home, name="home"),
    path("user_profile/<str:username>/", views.user_profile, name="user_profile"),
]
