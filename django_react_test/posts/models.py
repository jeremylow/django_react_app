# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
