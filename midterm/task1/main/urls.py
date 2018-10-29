from django.urls import path, re_path
from main import views

urlpatterns=[
    path('', views.home, name='home'),
    path('restaurant', views.resta, name='restaurant'),

]