"""Defines URL patterns for pizzeria."""

from django.urls import path

from . import views

app_name = 'pizzeria'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Menu
    path('menu', views.pizzas, name='menu'),
    # Pizza
    path('menu/<int:pizza_id>', views.pizza, name='pizza')
]