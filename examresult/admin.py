from django.contrib import admin
from .models import Test, Question, ExamResult

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'active']
    inlines = [QuestionInline]



@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'test__name', 'score', 'completed_at']



