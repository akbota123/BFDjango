from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.list),
    path('1/completed/', views.complete)
]