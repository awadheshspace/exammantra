
from django.contrib import admin
from .models import eBook, Tag

class eBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'description')

admin.site.register(eBook, eBookAdmin)
admin.site.register(Tag)