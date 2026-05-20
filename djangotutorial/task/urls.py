from django.urls import path, re_path
from .views import task_list, task_detail, task_create, task_edit, task_delete, task_statistics

urlpatterns = [
    # Список задачь
    path('', task_list, name='task_list'),

    # Детальный обзор задачи
    path('<int:pk>/', task_detail, name='task_detail'),

    # Создание задачи
    path('create/', task_create, name='task_create'),

    # Редактирование задачи
    # re_path(r'(?P<pk>\d+)/$)', task_edit, name='task_edit'),

    # Удаление задачи
    # re_path(r'(?P<pk>\d+)/$)', task_delete, name='task_delete'),

    # Статистика по задачам
    path('statistics/', task_statistics, name='statistics'),
]