from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name


