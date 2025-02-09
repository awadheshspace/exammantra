from django.contrib import admin
from django.urls import include, path
from exammantra import views
# from . import views

app_name = 'exammantra'
urlpatterns = [
   
    # path('signup',views.signup_page,name="signup"),
    # path('login/',views.login_page,name="login"),
    path('',views.main_page, name="mainpage"),
    path('notes/', views.notes_list, name='notes_list'),
   
]
