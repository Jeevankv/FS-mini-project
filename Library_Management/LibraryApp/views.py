from django.shortcuts import render, redirect
from django.contrib import messages
from . import main
from django.core.files import File



def login(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        password = request.POST.get('password')
        pos = main.binary_search('index.txt', str(uid))
        if pos == -1:
             messages.warning(request,"User ID is Incorrect!. Please Re-enter")  
             return redirect('library-login')
        else:
            f2 = open ('Userprofile.txt', 'r')
            f2.seek(int(pos))
            l = f2.readline()
            l = l.rstrip()
            word = l.split('|')
            if(main.verify_password(word[1], password)):
                messages.success(request,"Login Successful!")  
                return redirect('library-home')
            else:
                messages.warning(request,"Password that you have entered is Incorrect.Please Re-enter") 
                return redirect('library-login' )
            f2.close()


    else:
        return render(request, 'login.html',)

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
        password = request.POST.get('password')
        if email == 'jeevankv18@gmail.com' and password == 'admin':
            return redirect('library-adminhome')
        return redirect('library-admin')
    else:
        return render(request, 'adminlogin.html')




def adminhome(request):

    return render(request, 'adminhome.html')


def libraryindex(request):
    return render(request, 'index.html')


def addbooks(request):
    if request.method == 'POST':
        bid = request.POST.get('bid')
        bname = request.POST.get('bname')
        aname = request.POST.get('aname')

        if len(str(bname)) == 0:
            messages.warning(request,"Missing Book Name") 
            return redirect('library-addbooks')
        
        if len(str(bid))!=5 or str(bid).isdigit() == False:
            messages.warning(request,"Please renter the details(ID should be 5 positive integers)")
            return redirect('library-addbooks')

        if len(str(aname)) == 0:
            aname = str(aname)
            aname = "Anonymous"

        pos = main.binary_search('Bindex.txt', str(bid))

        if pos != -1:
            messages.warning(request,"Book already present.Please try again")
            return redirect('library-addbooks')

        f22 = open ('BData.txt', 'a')
        pos = f22.tell()
        f33 = open ('Bindex.txt', 'a')
        buf = str(bid) + '|' + str(bname) + '|' + str(aname) + '|' + 'Y' + '|' + '#'
        f22.write(buf)
        f22.write('\n')
        buf = str(bid) + '|' + str(pos) + '|' + '#'
        f33.write(buf)
        f33.write('\n')
        f33.close()
        f22.close()
        main.key_sort('Bindex.txt')
        messages.success(request,"Book added Successfully!")
        return redirect('library-addbooks')

    else:
        return render(request, 'addbooks.html')


def reopen_login(request):
	f7=open('Bindex.txt','r')
	lines1=f7.readlines()
	f7.close()
	f8=open('Bindex.txt','w')
	for line1 in lines1:
		if line1.startswith('*'):
			continue
		else:
			f8.write(line1)
	f8.close()
	return render(request,'reopenLogin.html')

def borrowbook(request):
    pass

def returnbook(request):
    pass