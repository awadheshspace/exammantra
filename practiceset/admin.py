from django.contrib import admin
from .models import CustomUser, PracticeMaterial


@admin.register(PracticeMaterial)
class PracticeMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'stream')