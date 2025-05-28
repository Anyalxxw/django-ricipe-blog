from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    name = models.TextField(max_length=100, unique=True)
    image = models.ImageField(blank=True, default='default.png')
    description = models.TextField()
    prep_time = models.PositiveIntegerField(default=15)
    cook_time = models.PositiveIntegerField(default=30)
    serving = models.PositiveIntegerField(default=3)
    ingredients = models.TextField()
    instruction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name