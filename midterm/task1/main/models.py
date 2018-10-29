from django.db import models


# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    number=models.IntegerField()
    telephone=models.IntegerField()
    city=models.CharField(max_length=30)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "#{}: {}".format(self.name, self.telephone)


class Dish(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=255)
    price=models.CharField(max_length=10)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "#{}: {}".format(self.name, self.description)


class Review(models.Model):
    rating=models.IntegerField()
    comment=models.TextField(max_length=255)
    date=models.DateField()

    def __str__(self):
        return self.rating


class RestaurantReview(models.Model):
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review=models.ForeignKey(Review, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.restaurant


class DishReview(models.Model):
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE)
    review=models.ForeignKey(Review, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish