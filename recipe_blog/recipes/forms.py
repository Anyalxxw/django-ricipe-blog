from .models import Recipe
from django import forms

class CreateRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'image', 'description', 'prep_time', 'cook_time', 'serving', 'ingredients', 'instruction']
        
    