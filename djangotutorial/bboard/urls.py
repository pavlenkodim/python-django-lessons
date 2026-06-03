from django.urls import path
from .views import index, by_rubric, BbCreateView, CommentCreateView, comment_list, comment_detail, comment_delete

# app_name='bboard'
urlpatterns = [
    path('<int:bd_pk>/comments/<int:sms_id>/delete', comment_delete, name='comment-delete'),
    path('<int:bd_pk>/comments/<int:sms_id>/',  comment_detail, name='comment-detail'),
    path('<int:bd_pk>/comments/create/',    CommentCreateView.as_view(), name='comment-create'),
    path('<int:bd_pk>/comments/',           comment_list,   name='comment-list'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]