
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class eBook(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='ebooks/pdfs/')
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.CharField(max_length=50, choices=[
        ('tech', 'Technology'),
        ('board', 'Board Exams'),
        ('competitive', 'Competitive Exams'),
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='ebooks/thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.title


#add s to profile and remove User from parameter and add setting.AUTH_USER_MODEL
class UserProfile(models.Model):
    user = models.OneToOneField( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stream = models.CharField(max_length=20, choices=[
        ('board', 'Board Exam'),
        ('tech', 'Tech Exam'),
        ('competitive', 'Competitive Exam')
    ])
    
       