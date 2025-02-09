from django.db import models
from django.contrib.auth.models import User



class PDFNote(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical Notes'),
        ('board', 'Board Exam Notes'),
    ]
    
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    pdf_file = models.FileField(upload_to='pdf_notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.topic}"


