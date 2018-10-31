from django import forms
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview


class RestoForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields=('name', 'telephone', 'city', 'user')