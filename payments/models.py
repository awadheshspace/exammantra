from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings  


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    paid_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    @property
    def calculate_due_fee(self):
        return self.total_fee - self.paid_fee

    def __str__(self):
        return self.full_name



class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255,default=1)
    status = models.CharField(max_length=50, choices=[('success', 'Success'), ('failed', 'Failed')])

    def __str__(self):
        return f'Payment {self.payment_id} for Order {self.order_id}'    