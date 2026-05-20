from django.forms import ModelForm
from .models import Task

class BbFrom(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'priority', 'deadline')
