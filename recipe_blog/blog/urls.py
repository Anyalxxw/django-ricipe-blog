from django.contrib import admin
from django.urls import path, include
from . import views

app_name='blog'

urlpatterns = [
    path('blog_list', views.blog_list, name='blog-list'),
    path('create_blog', views.create_post, name='create-blog')
]
