from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, StreamChoiceForm, PracticeMaterialForm
from .models import PracticeMaterial
from django.contrib.auth.models import User
from examresult.views import test_list
from examresult import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Add these views

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if not user.stream:
#                 return redirect('practiceset:stream_choice')
#             return redirect('examresult:test_list')
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'practice/login.html')



# @login_required
# def test_list(request):
#     return render(request, 'examresult/exam/test_list.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next')
                
                if next_url:
                    return redirect(next_url)  
                else:
                    return redirect('examresult:test_list')
            else:
                messages.success(request, 'Invalid username or password')
        except:
            messages.success(request, 'Something went Wrong , Reclose The Site and Open Again')

    next_url = request.GET.get('next')
    return render(request, 'practice/login.html', {'next': next_url})

    

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully...... Please login again To Access the Resources') 
    return redirect('practiceset:login')



def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('practiceset:stream_choice')
            return redirect('practiceset:registration_sucess') 
        else:
            messages.error(request, 'Enter The Correct Details, Please Try Again')
    else:
        form = RegistrationForm()
    return render(request, 'practice/register.html', {'form': form})
    
    # return render(request, 'practice/register.html', {'form': form})

def registration_sucess(request):
    return render(request, 'practice/registration_sucess.html')

@login_required(login_url='/accounts/login/')
def stream_choice_view(request):
    if request.method == 'POST':
        form = StreamChoiceForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('practiceset:materials')
    else:
        form = StreamChoiceForm(instance=request.user)
    return render(request, 'practice/stream_choice.html', {'form': form})

@login_required
def materials_view(request):
    if not request.user.stream:
        return redirect('practiceset:stream_choice')
    
    materials = PracticeMaterial.objects.filter(category=request.user.stream)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        materials = materials.filter(title__icontains=search_query)
    
    return render(request, 'practice/materials.html', {
        'materials': materials,
        'search_query': search_query
    })
