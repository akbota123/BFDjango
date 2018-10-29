from django.forms import ModelForm
from django import forms
from .models import User, Restaurant, Dish, Review


class UserForm(ModelForm):
    class Meta:
        model=User
        fields=('fisrt_name', 'second_name', 'email')


class RestaurantForm(ModelForm):
    class Meta:
        model=Restaurant
        fields=('name', 'number', 'telephone', 'city')


class DishForm(ModelForm):
    class Meta:
        model=Dish
        fields=('name', 'description', 'price')


class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=('rating', 'comment', 'date')
