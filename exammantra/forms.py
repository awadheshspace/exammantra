from django import forms
from .models import PDFNote
from .models import PracticePaper, UserProfiles

class PDFNoteForm(forms.ModelForm):
    class Meta:
        model = PDFNote
        fields = ['subject', 'topic', 'category', 'pdf_file']

