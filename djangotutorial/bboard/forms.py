from django.forms import ModelForm
from .models import Bd

class BbFrom(ModelForm):
    class Meta:
        model = Bd
        fields = ('title', 'content', 'price', 'rubric', 'kind')
