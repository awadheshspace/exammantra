from django.contrib import admin
from .models import Course, Module, Video, PDFNotes


class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

class VideoInline(admin.StackedInline):
    model = Video
    extra = 1

class PDFNotesInline(admin.StackedInline):
    model = PDFNotes
    extra = 1



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'instructor', 'price', 'created_at')
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    inlines = [VideoInline, PDFNotesInline]
    ordering = ('course', 'order')