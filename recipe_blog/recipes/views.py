from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import CreateRecipe
from .models import Recipe
from django.contrib.auth.decorators import login_required

# Create your views here.
def recipe(request, name):
    recipe = get_object_or_404(Recipe, name=name)
    instructions = recipe.instruction.split('\n')
    ingredients = recipe.ingredients.split('\n')
    return render(request, 'recipe.html', {
        'recipe': recipe,
        'instructions': instructions,
        'ingredients': ingredients
        })

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipe(request.POST, request.FILES)
        if form.is_valid():  
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipes:recipes-list')
    else:
        form = CreateRecipe()
    return render(request, 'create-recipe.html', {'form': form})

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes-list.html', {'recipes': recipes})