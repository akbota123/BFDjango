from django.urls import path, include
from . import views

urlpatterns=[
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('advert_list/', views.AdvertList.as_view()),
    path('advert_detail/<int:pk>/', views.AdvertDetail.as_view()),
    path('advertlist/', views.advert_list),
    path('advertdetail/<int:pk>/', views.advert_detail),
]