from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard-login/', views.dashboard_login, name='dashboard_login'),
    path('logout/', views.logout_views, name='logouts'),
    path('upload/', views.upload_assignment, name='upload_assignment'),
    path('view/', views.view_assignments, name='view_assignments'),
]