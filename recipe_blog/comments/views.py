from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateComment
from .models import Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def make_comment(request):
    if request.method == 'POST':
        form = CreateComment(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home-page')
    else:
        form = CreateComment()
    return render(request, 'make-comment.html', {'form': form})