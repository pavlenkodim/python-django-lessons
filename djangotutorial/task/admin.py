from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'deadline', 'is_done', 'created_at')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description')

# Register your models here.
admin.site.register(Task, TaskAdmin)
