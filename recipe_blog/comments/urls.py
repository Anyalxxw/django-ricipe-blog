from django.contrib import admin
from django.urls import path, include
from . import views

app_name='comments'

urlpatterns = [
    path('make-comment', views.make_comment, name='make-comment'),
]
