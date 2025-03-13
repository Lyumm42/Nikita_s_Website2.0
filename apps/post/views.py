from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "post/list.html", {"posts": posts})

