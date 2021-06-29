from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import CommentForm


def post_list(request):
    post = Post.objects.filter(moder=True)
    return render(request, 'post/post_list.html', {'posts': post})


def post_single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # comment = CommentPost.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.user = request.user
            comm.post = post
            comm.save()
    else:
        form = CommentForm()
    return render(request, 'post/post_single.html', {'post': post, 'form': form})
