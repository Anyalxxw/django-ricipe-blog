from django.contrib import admin
from django.urls import path, include
from . import views 

app_name='recipes'

urlpatterns = [
    path('recipes_list/', views.recipes_list, name='recipes-list'),
    path('create_recipe/', views.create_recipe, name='create-recipe'),
    path('recipes/<str:name>/', views.recipe, name='recipe'),
]
