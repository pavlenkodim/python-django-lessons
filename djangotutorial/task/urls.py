from django.urls import path, re_path
from . import views

app_name = 'task'
urlpatterns = [
    # Список задач
    path('', views.task_list, name='task_list'),

    # Детальный обзор задачи
    path('<int:task_id>/', views.task_detail, name='task_detail'),

    # Создание задачи
    path('create/', views.task_create, name='task_create'),

    # Редактирование задачи
    re_path(r'^(?P<task_id>\d+)/edit/$', views.task_edit, name='task_edit'),

    # Удаление задачи
    re_path(r'^(?P<task_id>\d+)/delete/$', views.task_delete, name='task_delete'),

    # Статистика по задачам
    path('statistics/', views.task_statistics, name='statistics'),
]