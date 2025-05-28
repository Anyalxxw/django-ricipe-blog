from django.http import HttpResponse
from django.shortcuts import render 
from comments.models import Comment
from recipes.models import Recipe


def home_page(request):
    comments = Comment.objects.all()
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {
        'comments': comments,
        'recipes': recipes
        })
















