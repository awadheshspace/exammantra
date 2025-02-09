from django.contrib import admin
from .models import PDFNote



@admin.register(PDFNote)
class PDFNoteAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic', 'category', 'uploaded_at')
    list_filter = ('category', 'subject')
    search_fields = ('subject', 'topic')



