from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    
    path('contact/', views.contact_page, name='contact_page'),
    path('submission_success/', views.submission_success, name='submission_success'),

]