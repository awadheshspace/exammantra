from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, PracticeMaterial

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class StreamChoiceForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['stream']
        widgets = {
            'stream': forms.RadioSelect
        }

class PracticeMaterialForm(forms.ModelForm):
    class Meta:
        model = PracticeMaterial
        fields = ['title', 'description', 'file', 'category']