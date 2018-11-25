from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class Advert(models.Model):
    title=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    number_views=models.IntegerField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text=models.TextField()
    email=models.EmailField()
    review=models.CharField(max_length=100)
    owner=models.ForeignKey(Advert, on_delete=models.CASCADE)

    def __str__(self):
        return self.review

