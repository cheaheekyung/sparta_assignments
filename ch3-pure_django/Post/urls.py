from django.urls import path
from . import views

app_name = "Post"
urlpatterns = [
    path("", views.post_list, name="post_list"),  # 게시글 목록
    path("<int:pk>/", views.post_detail, name="post_detail"),  # 게시글 상세
    path("create/", views.post_create, name="post_create"),  # 게시글 작성
    path("<int:pk>/edit/", views.post_edit, name="post_edit"),  # 게시글 수정
    path("<int:pk>/delete/", views.post_delete, name="post_delete"),  # 게시글 삭제
]
