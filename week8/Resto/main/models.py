from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
    name=models.CharField(max_length=200)
    number=models.CharField(max_length=10)
    telephone=models.CharField(max_length=15)
    city=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description=models.TextField(max_length=300)
    price=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='meal')

    def __str__(self):
        return self.name


class Review(models.Model):
    rating=models.CharField(max_length=10)
    comment=models.TextField(max_length=200)
    date=models.DateField()

    def __str__(self):
        return self.rating


class RestaurantReview(models.Model):
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restview')
    review=models.ForeignKey(Review, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant.__str__()


class DishReview(models.Model):
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dishview')
    review=models.ForeignKey(Review, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish.__str__()