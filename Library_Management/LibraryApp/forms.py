from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    uid =forms.CharField()
    name =forms.CharField()
    email =forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
       fields =['uid','username','email','password'] 