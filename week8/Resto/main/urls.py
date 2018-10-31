from django.contrib import admin
from django.urls import path, include
from . import views
from .views import FirstView, RestaurantView, CreateRestView, DeleteView, DishesView
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('', FirstView.as_view(), name='home'),
    path('<int:pk>/', RestaurantView.as_view()),
    path('add/', login_required(CreateRestView.as_view()), name='add'),
    path('<int:fk>/review/<int:pk>/', login_required(DishesView.as_view()), name='dishes'),
    path('<int:fk>/delete/<int:pk>/', login_required(DeleteView.as_view())),
]