from django.views.generic import (
    DetailView, DeleteView, CreateView, UpdateView,
)
from django.urls import reverse_lazy
from django_filters.views import FilterView

from .models import Task
from .forms import TaskForm, TaskUpdateForm
from .filters import TaskFilter


class TaskListView(FilterView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:list')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:list')
    

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:list')