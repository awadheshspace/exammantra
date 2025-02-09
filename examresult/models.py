from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Test(models.Model):
    name = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.PositiveIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])

class ExamResult(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)
