from django.shortcuts import render, redirect
from .forms import InquiryForm
from .models import Inquiry

# def contact_page(request):
#     if request.method == 'POST':
#         form = InquiryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_page')
#     else:
#         form = InquiryForm()
#     return render(request, 'contact/contact.html', {'form': form})


def contact_page(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submission_success')  # Redirect to success page
    else:
        form = InquiryForm()
    return render(request, 'contact/contact.html', {'form': form})

def submission_success(request):
    return render(request, 'contact/submission.html')