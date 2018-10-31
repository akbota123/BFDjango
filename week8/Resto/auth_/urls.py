from django.urls import path
from django.contrib import admin
from auth_ import views

urlpatterns=[
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]