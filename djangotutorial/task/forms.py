from django.forms import ModelForm
from .models import Task

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'deadline')

class TaskEditForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'deadline', 'is_done')