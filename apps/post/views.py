from django.shortcuts import render, redirect
from apps.post.forms import PostForm


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return render(request, 'post/create_post.html',{'form': form})
    else:
        form = PostForm()
        return render(request, 'post/create_post.html',{'form': form})