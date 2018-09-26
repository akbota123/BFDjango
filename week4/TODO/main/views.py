from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import Task, Person
#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")


def list(request):
    list_todo=Task.objects.filter(mark=False)
    context={'l': list_todo}
    return render(request, 'todo_list.html', context)


def complete(request):
    list_of_completed=Task.objects.filter(mark=True)
    context={'keys': list_of_completed}
    return render(request, 'completed_todo_list.html', context)