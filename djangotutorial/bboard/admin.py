from django.contrib import admin
from .models import Bd, Rubric, Comment


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

# Register your models here.
admin.site.register(Comment)
admin.site.register(Rubric)
admin.site.register(Bd, BdAdmin)
