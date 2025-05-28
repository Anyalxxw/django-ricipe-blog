from django.db import models

# Create your models here.
class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, default='default.png')
    
    def __str__(self):
        return self.title