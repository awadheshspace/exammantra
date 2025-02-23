from django.contrib import admin
from django.urls import include, path
from exammantra import views
# from . import views

app_name = 'exammantra'
urlpatterns = [
    
    path('',views.main_page, name="mainpage"),
    path('notes/', views.notes_list, name='notes_list'),
   
]
