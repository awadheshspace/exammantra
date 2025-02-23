# assignments/admin.py
from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'submission_date', 'file')

admin.site.register(Assignment, AssignmentAdmin)
