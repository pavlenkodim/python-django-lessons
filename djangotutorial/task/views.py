from django.db.models.aggregates import Sum, Min, Max
from django.shortcuts import render

from task.models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

def task_create(request):
    return render(request, 'task/task_create.html')

def task_edit(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task/task_edit.html', {'task': task})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task/task_delete.html', {'task': task})

def task_statistics(request):
    statistics = Task.objects.aggregate(
        total=Sum('priority'),
        min=Min('priority'),
        max=Max('priority'),
    )
    context = {'total': statistics['total'], 'min': statistics['min'], 'max': statistics['max']}

    return render(request, 'task/task_statistics.html', context)