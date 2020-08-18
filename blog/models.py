from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.pk)))


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=50, default='blogtag')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='lol')
    summary = models.TextField(default='null')


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.pk)))
