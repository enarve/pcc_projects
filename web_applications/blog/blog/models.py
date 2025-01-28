from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    def __str__(self):
        return self.title

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    def __str__(self):
        return self.title