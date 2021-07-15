from django.shortcuts import render, redirect
from django.contrib import messages
from . import main
from django.core.files import File



def login(request):
    return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        uid = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
    
    
        if len(str(uid))==0 or len(str(name)) == 0 or len(str(email)) == 0 or len(str(password)) == 0:
            messages.warning(request,"You left one or more fields blank")
            return redirect('library-register')  

        pos = main.binary_search('index.txt', str(uid))
        if pos!=-1:
            messages.warning(request,"Already registered. Choose a different ID")
            return render(request, 'register.html')
        else:
            f2 = open('Userprofile.txt','a')
            pos = f2.tell()
            f3 = open('index.txt','a')
            buf = str(uid) + '|' + main.hash_password(str(password)) + '|' + str(name) + '|' + str(email) + '|' + '#'

            f2.write(buf)
            f2.write('\n')
            buf = str(uid) + '|' + str(pos) + '|' + '#'
            f3.write(buf)
            f3.write('\n')
            f3.close()
            f2.close()
            main.key_sort('index.txt')
            messages.success(request,"Registration Successful!") 
            return redirect('library-login')  
             

    else: 
        return render(request, 'register.html')

def adminLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('passwo rd')
        if email == 'jeevankv18@gmail.com' and password == 'admin':
            return redirect('library-adminhome')
    return render(request, 'adminlogin.html')





def adminhome(request):
    return render(request, 'adminhome.html')