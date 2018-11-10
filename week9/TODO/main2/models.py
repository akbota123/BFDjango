from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your models here.


class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Task(models.Model):
    name=models.CharField(max_length=100)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE),
    due_on=models.DateField()
    email=models.EmailField()

    objects=TaskManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('main2:')


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    tasks=models.ForeignKey(Task, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.first_name
