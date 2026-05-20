from django.db.models.aggregates import Sum, Min, Max, Count
from django.shortcuts import render, redirect

from task.models import Task
from .forms import TaskEditForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    # Исключить поле(я)
    # tasks = Task.objects.defer('priority')
    # Выбрать только эти ...
    # tasks = Task.objects.only('title', 'description', 'priority', 'status' )

    return render(request, 'task/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'task/task_detail.html', {'task': task})

def task_create(request):
    return render(request, 'task/task_create.html')

def task_edit(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task_id)
    else:
        form = TaskEditForm(instance=task)

    return render(request, 'task/task_edit.html', {'form': form})

def task_delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task_list')

def task_statistics(request):
    statistics = Task.objects.aggregate(
        total=Sum('priority'),
        min=Min('priority'),
        max=Max('priority'),
        count=Count('title')
    )
    # context = {'total': statistics['total'], 'min': statistics['min'], 'max': statistics['max'], 'count': statistics['count']}

    return render(request, 'task/task_statistics.html', statistics)