from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import register_view, login_view, logout_view

app_name = 'practiceset'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('stream-choice/', views.stream_choice_view, name='stream_choice'),
    path('materials/', views.materials_view, name='materials'),
    path('registration_sucess/', views.registration_sucess, name='registration_sucess'),

]
