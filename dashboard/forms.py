# assignments/forms.py
from django import forms
from .models import Assignment

class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'file']
