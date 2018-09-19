from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import date


def tasks(request):
    now=date.today()
    tasks=[{
        'Task':'Task {}'.format(i),
        'Created': now.strftime("%d/%m/%y"),
        'Due': now.replace(day=now.day + 2).strftime("%d/%m/%y"),
        'Owner': 'admin',
        'Mark': 'Done',
        'Complete': False}
        for i in range(1, 5)]
    context={'tasks': tasks}
    return render(request, 'todo_list.html', context)


def completed_tasks(request):
    now = date.today()
    tasks = {
        'Task': 'Task 0',
        'Created': now.strftime("%d/%m/%y"),
        'Due': now.replace(day=now.day + 2).strftime("%d/%m/%y"),
        'Owner': 'admin',
        'Mark': 'Not Done',
        'Complete': True
    }
    return render(request, 'completed_todo_list.html', tasks)