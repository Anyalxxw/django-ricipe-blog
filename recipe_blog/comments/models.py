from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, default='default.png')
    name = models.TextField(max_length=100)
    
    def __str__(self):
        return self.text    