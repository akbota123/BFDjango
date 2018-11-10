from django.urls import path
from main2.views import views


app_name='main2'

urlpatterns=[
    #path('about/', views.AboutView.as_view(), name='about'),
    #path('detail/', views.DetailView.as_view(template_name='detail.html'), name='detail'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]