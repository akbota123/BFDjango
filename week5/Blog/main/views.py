from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import Post, Comment

# Create your views here.

def new_post(request):
    return render(request)


