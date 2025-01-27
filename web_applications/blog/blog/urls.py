from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('blogs/<int:blog_id>', view=views.blog, name='blog'),
    path('posts/<int:post_id>', view=views.post, name='post'),
]
