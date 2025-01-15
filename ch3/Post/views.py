from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})


@login_required
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect("Post:post_list")
    return render(request, "post_form.html")


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("Post:post_detail", pk=post.pk)
    return render(request, "post_form.html", {"post": post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("Post:post_list")
    return render(request, "post_confirm_delete.html", {"post": post})
