from django.contrib import admin
from .models import Student,Payment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'full_name', 'father_name', 'total_fee', 'paid_fee', 'due_fee')
    search_fields = ('roll_number', 'full_name')
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'payment_date', 'status')
    list_filter = ('status', 'payment_date')