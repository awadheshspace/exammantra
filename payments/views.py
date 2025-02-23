from urllib import request
import razorpay
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import PaymentForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from decimal import Decimal

from django.conf import settings
import hashlib



client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


@login_required
def fee_dashboard(request):
    students = Student.objects.all().order_by('roll_number')
    return render(request, 'payments/admin_dashboard.html', {'students': students})


@login_required
def student_payment(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)

    

    return render(request, 'payments/student_payment.html', {
        'student': student,
        
    })

# def pay_fee(request):   
#     return render(request,'payments/payment_success.html')