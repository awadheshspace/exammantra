# assignments/models.py
from django.db import models
from django.conf import settings  # Import settings

class Assignment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='assignments/')
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.student.username}'
