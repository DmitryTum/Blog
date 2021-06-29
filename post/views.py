from django.shortcuts import render, get_object_or_404
from .models import *


def post_list(request):
    post = Post.objects.filter(moder=True)
    return render(request, 'post/post_list.html', {'posts': post})


def post_single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_single.html', {'post': post})
