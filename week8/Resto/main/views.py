from django.shortcuts import render, redirect
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview
from .forms import RestoForm
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

class FirstView(View):
    def get(self, request):
        return render(request, 'home.html')


class RestaurantView(View):
    def get(self, request, pk):
        rests=Restaurant.objects.get(pk=pk)
        context={
            'restaurant':rests,
        }
        return render(request, 'home.html', context)


class CreateRestView(View):
    def get(self, request):
        form=RestoForm
        context={
            'form':form,
            'restaurant':Restaurant.objects.all(),
            'users':User.objects.all()
        }
        return render(request, 'addRest.html', context)

    def post(self, request):
        form=RestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


class DishesView(View):
    def get(self, request, pk, fk):
        resto=Restaurant.objects.get(pk=pk)
        dishes=resto.dishes.all()
        reviews=RestaurantReview.objects.filter(restaurant=pk)
        context={
            'resto':resto,
            'dishes':dishes,
            'reviews':reviews,
        }
        return render(request, 'dishes.html', context)


class DeleteView(View):
    def get(self, request, pk, fk):
        resto=Restaurant.objects.get(pk=pk)
        resto.delete()
        return redirect('home')
