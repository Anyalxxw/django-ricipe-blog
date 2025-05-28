from . import models
from django import forms

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'text', 'image']