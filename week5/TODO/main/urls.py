from django.urls import path, re_path
from django.contrib import admin
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.list, name='todos'),
    path('completed/', views.complete, name="completed"),
    re_path(r'^todos/([\w\_?]+)/order_by/$', views.list_filter, name='order_by'),
    re_path(r'^todos/completed/([\w\_?]+)/order_by/$', views.complete_filter, name='completed_order_by'),
    path('add/', views.add, name="add"),
    re_path(r'^todos/(\d+)/change_mark/$', views.done, name="done"),
    re_path(r'^todos/(\d+)/delete/$',views.delete,name="delete"),
    re_path(r'^todos/(\d+)/owner/$', views.detail, name="detail"),
]