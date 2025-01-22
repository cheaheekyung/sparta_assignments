from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.ArticleList.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetail.as_view(), name="article_detail"),
    path("<int:pk>/comments/", views.CommentList.as_view(), name="comment_list"),
    path(
        "comments/<int:comment_pk>/",
        views.CommentDetail.as_view(),
        name="comment_detail",
    ),
]
