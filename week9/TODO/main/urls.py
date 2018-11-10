from django.urls import path
from main import views

urlpatterns=[
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='list'),
    path('tasks/add/', views.task_add, name='add'),
]