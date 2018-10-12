from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import Task, Person
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


# def index(request):
# return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, 'home.html')


@login_required
def list(request):
    tasks = Task.objects.all()
    context = {'Task': tasks}
    return render(request, 'completed_todo_list.html', context)


def list_filter(request, f):
    task = Task.objects.order_by(f)
    context = {'Task': task}
    return render(request, 'todo_list.html', context)


@login_required
def complete(request):
    tasks = Task.objects.filter(mark=True)
    completed = {'Task': tasks}
    return render(request, 'completed_todo_list.html', completed)


def complete_filter(request, f):
    task = Task.objects.filter(mark=True).order_by(f)
    context = {'Task': task}
    return render(request, 'completed_todo_list.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = TaskForm()
        context = {'form': form}
        return render(request, 'add_task.html', context)


@login_required
def detail(request, task_id):
    owner = Person.objects.get(id=task_id)
    context = {'owner': owner, 'tasks': owner.tasks.all()}
    return render(request, 'task_detail.html', context)


def delete(request, task_id):
    task = Task.objects.delete()
    context = {'Task': task}
    return render(request, 'list.html', context)



def done(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.mark == False:
        task.mark = True
    else:
        task.mark = False
    task.save()
    task = Task.objects.all()
    context = {'Task': task}
    return render(request, "list.html", context)



