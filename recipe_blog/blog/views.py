from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreatePost
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:blog-list')
    else:
        form =  CreatePost()
    return render(request, 'create-blog.html', {'form': form})