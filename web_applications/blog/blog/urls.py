from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('blogs/<int:blog_id>', view=views.blog, name='blog'),
    path('posts/<int:post_id>', view=views.post, name='post'),
    path('make_blog', view=views.make_blog, name='make_blog'),
    path('make_post/<int:blog_id>', view=views.make_post, name='make_post'),
    path('edit_post/<int:post_id>', view=views.edit_post, name='edit_post'),
]
