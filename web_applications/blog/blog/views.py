from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm

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
        'blog': post.blog,
        'post': post
    }
    return render(request, 'blog/post.html', context=context)

@login_required
def make_blog(request):
    if request.method != 'POST':
        form = BlogForm()

    else:
        data = request.POST
        form = BlogForm(data)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            return redirect('blog:index')

    context = {
        'form': form
    }
    return render(request, 'blog/make_blog.html', context=context)

@login_required
def make_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method != 'POST':
        form = BlogPostForm()

    else:
        data = request.POST
        form = BlogPostForm(data)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
            return redirect('blog:blog', blog.id)

    context = {
        'form': form,
        'blog': blog
    }
    return render(request, 'blog/make_post.html', context=context)

@login_required
def edit_post(request, post_id):
    
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    if blog.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = BlogPostForm(instance=post)

    else:
        data = request.POST
        form = BlogPostForm(instance=post, data=data)
        if form.is_valid():
            form.save()
            return redirect('blog:post', post.id)

    context = {
        'form': form,
        'post': post,
        'blog': blog,
    }
    return render(request, 'blog/edit_post.html', context=context)