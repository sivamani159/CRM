from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    pwd=forms.CharField(label='password',widget=forms.PasswordInput)

class DemoForm(forms.ModelForm):
    class Meta:
        model=Demo
        fields='__all__'
        fields = ['did','coursename','faculty','event_date', 'event_time','demotype']
        widgets = {
            'event_date': forms.DateInput(format='%Y-%m-%d'),
            'event_time': forms.TimeInput(format='%H:%M'),
        }
        input_formats = {
            'event_date': ['%Y-%m-%d'],
            'event_time': ['%H:%M'],
        }


class CreateStaffForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2','is_staff']

class CreateUserForm(UserCreationForm):
   
    class Meta:
        model=User
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'vcube@123'}))
        fields=['username','email','password1','password2']


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


