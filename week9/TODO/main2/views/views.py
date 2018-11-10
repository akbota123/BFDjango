from django.urls import reverse_lazy
from django.views.generic import (
TemplateView,
ListView,
DeleteView,
DetailView,
CreateView,
UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from main2.models import Task, Author
from main2.forms import AuthorForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'



class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'due_on', 'email']
    success_url = reverse_lazy('main2:task_list')
    template_name = 'main2/task_form.html'

    def form_valid(self, form):
        form.instance.created_by=self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('main2:task_form')

    def get_queryset(self):
        return Task.objects.for_user(user=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    #peresmotret
    form_class = AuthorForm
    success_url = reverse_lazy('main2:task_form')

    def get_queryset(self):
        return Task.objects.for_user(user=self.request.user)
