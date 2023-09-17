from django.contrib import admin

from .models import Question


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'status']
    ordering = ['question_text']
    actions = [make_published]

admin.site.register(Question, QuestionAdmin)