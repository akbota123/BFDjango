from django.db import models
from django.utils.datetime_safe import time

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    name_t=models.CharField(max_length=100)
    created=models.DateField()
    dueon=models.DateField()
    owner=models.ForeignKey(Person, on_delete=models.CASCADE)
    mark=models.BooleanField()

    def __str__(self):
        return "{},{},{},{}".format(self.name_t, self.created, self.dueon, self.owner)

