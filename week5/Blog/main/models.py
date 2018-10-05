from django.db import models
from django.utils.datetime_safe import time

# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):


    def __str__(self):
        return
