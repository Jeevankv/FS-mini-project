from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
def login(request):
    return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
            data = request.POST
            print(data)  
    return render(request, 'register.html')





def adminLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == 'jeevankv18@gmail.com' and password == 'admin':
            return redirect('library-adminhome')
    return render(request, 'adminlogin.html')





def adminhome(request):
    return render(request, 'adminhome.html')