from django.forms import ModelForm
from .models import Bd, Comment

class BbFrom(ModelForm):
    class Meta:
        model = Bd
        fields = ('title', 'content', 'price', 'rubric', 'kind')

class BbCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')