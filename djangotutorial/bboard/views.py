from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Bd, Rubric
from .forms import BbFrom

# Controller
class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbFrom
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


# Create your views here.
def index(request):
    bbs = Bd.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs, 'rubrics': rubrics})

def by_rubric(request, rubric_id):
    bbs = Bd.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)