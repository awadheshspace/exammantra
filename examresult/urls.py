from django.urls import path
from . import views

app_name = 'examresult'
#
urlpatterns = [
    path('tests/', views.test_list, name='test_list'),
    path('test/<int:test_id>/', views.take_test, name='take_test'),
    path('result/<int:result_id>/', views.test_result, name='test_result'),
]

