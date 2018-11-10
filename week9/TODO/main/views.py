from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from main.models import Task, Author
from main.forms import AuthorForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required
def task_list(request):
    if request.user.is_authenticated:
        tasks=Task.objects.all()
        context={
            'tasks':tasks
        }
        return render(request, 'list.html', context)
    return redirect('login')


@login_required
def task_add(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=AuthorForm()
    context={
        'form':form
    }
    return render(request, 'add.html', context)