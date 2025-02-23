from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('fee/dashboard/', views.fee_dashboard, name='fee_dashboard'),
    path('payment/<str:roll_number>/', views.student_payment, name='student_payment'),
    # path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    # path('payment-handler/', views.payment_handler, name='payment_handler'),

]
