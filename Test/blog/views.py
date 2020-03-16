import os
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Terminal
from .forms import PostForm, TerminalForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def terminal(request):
    if request.method=='POST' and 'uname' in request.POST:
        output = os.popen('uname -a').read()
        return render(request, 'blog/terminal.html', {'output': output})
    if request.method=='POST' and 'ls' in request.POST:
        output = os.popen('ls').read()
        return render(request, 'blog/terminal.html', {'output': output})
    return render(request, 'blog/terminal.html', {'output': "0"})

def device_list(request):
    return render(request, 'blog/device_list.html', {})
