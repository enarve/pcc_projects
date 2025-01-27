from django.shortcuts import render
from .models import Blog, BlogPost

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/index.html', context=context)

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blogposts = blog.blogpost_set.order_by('-date')
    context = {
        'blog': blog,
        'blogposts': blogposts,
    }
    return render(request, 'blog/blog.html', context=context)

def post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context=context)