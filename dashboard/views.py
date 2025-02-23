from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
# from .models import PracticeMaterial
from django.contrib.auth.models import User
from examresult.views import test_list
from examresult import *
from django.contrib import messages
from .forms import AssignmentUploadForm
from .models import Assignment

def dashboard_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        try:
            if user is not None:
                login(request, user)
                return render(request, 'dash/dashboard_home.html')
            else:
                messages.success(request, 'Invalid username or password')
        except:
            return render(request, 'dash/dashboard_home.html')
            # messages.success(request, 'Something went Wrong , Reclose The Site and Open Again')

    return render(request, 'dash/dashboard_login.html')

    
def logout_views(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.....') 
    return redirect('dashboard:dashboard_login')


@login_required
def upload_assignment(request):
    if request.method == 'POST':
        form = AssignmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.student = request.user  # Associate the assignment with the logged-in student
            assignment.save()
            return redirect('dashboard:view_assignments')
    else:
        form = AssignmentUploadForm()
    return render(request, 'dash/upload_assignment.html', {'form': form})

@login_required
def view_assignments(request):
    assignments = Assignment.objects.filter(student=request.user)
    return render(request, 'dash/view_assignments.html', {'assignments': assignments})
