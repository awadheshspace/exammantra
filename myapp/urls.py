from django.contrib import admin
from django.urls import include, path
from myapp import views

urlpatterns = [
   
    path('signup',views.signup_page,name="signup"),
    path('login/',views.login_page,name="login"),
    path('home/page',views.home_page,name="home"),
    path('logout/',views.logout_page, name="logout"),
    path('dash',views.dashboard_page, name="dashboard"),
    path('index',views.index_page, name="index"),

]
