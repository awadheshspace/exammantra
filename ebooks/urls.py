from django.urls import path
from . import views

app_name = 'ebooks'

urlpatterns = [
    path('', views.ebook_list, name='ebook_list'),
]