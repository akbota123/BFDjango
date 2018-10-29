from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import User, Restaurant, Review, Dish, RestaurantReview, DishReview
from .forms import UserForm, RestaurantForm, DishForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def resta(request):
    resta=Restaurant.objects.all()
    context={'Restaurant':resta}
    return render(request, 'restaurant.html', context)


def resta_filter(request, rf):
    resta_f=Restaurant.objects.order_by(rf)
    context={'Restaurant':resta_f}
    return render(request, 'restaurant.html', context)


@login_required
def resta_add(request):
    if request.method=='POST':
        form=RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant')
    else:
            form=RestaurantForm()
    context={'form':form}
    return render(request, 'new.html', context)


@login_required
def dish(request):
    meal=Dish.objects.all()
    context={'Dish', meal}
    return render(request, 'dish.html', context)



