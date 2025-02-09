from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    STREAM_CHOICES = [
        ('board', 'Board Exam'),
        ('tech', 'Tech Exam'),
        ('competitive', 'Competitive Exam')
    ]
    stream = models.CharField(max_length=20, choices=STREAM_CHOICES, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
    )
    

class PracticeMaterial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='practice_materials/')
    category = models.CharField(max_length=20, choices=CustomUser.STREAM_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    