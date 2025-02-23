from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='course_thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

class Video(models.Model):
    module = models.ForeignKey(Module, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='course_videos/')
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)

class PDFNotes(models.Model):
    module = models.ForeignKey(Module, related_name='pdf_notes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='course_pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)

