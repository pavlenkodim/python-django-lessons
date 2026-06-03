from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .models import Bd, Rubric, Comment
from .forms import BbFrom, BbCommentForm


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

# Comments
# From AI Claude
def comment_list(request, bd_pk):
    bd = get_object_or_404(Bd, pk=bd_pk)
    comments = bd.comments.all()
    return render(request, 'bboard/comment_list.html', {'bd': bd, 'comments': comments})

def comment_detail(request, bd_pk, sms_id):
    comment = get_object_or_404(Comment, pk=sms_id, bd=bd_pk)
    return render(request, 'bboard/comment_detail.html', {'comment': comment})

def comment_delete(request, bd_pk, sms_id):
    comment = get_object_or_404(Comment, pk=sms_id, bd=bd_pk)
    comment.delete()
    return redirect('index')

class CommentCreateView(CreateView):
    model = Comment
    form_class = BbCommentForm
    template_name = 'bboard/comment_create.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.bd = get_object_or_404(Bd, pk=self.kwargs['bd_pk'])
        comment.save()
        return redirect('comment-list', bd_pk=self.kwargs['bd_pk'])