from django.shortcuts import render, redirect
from django.contrib import messages
from . import main

from datetime import timedelta, date


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


def libraryhome(request):
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

    headings = ("ID","Title","Author","Availability")
    data = list()
    f1 = open('Bindex.txt', 'r')
    f = open ("BData.txt", 'r')
    norecord = 0
    for line in f1:
        norecord += 1
        line = line.rstrip('\n')
        word = line.split('|')
        f.seek(int(word[1]))
        line1 = f.readline().rstrip()
        word1 = line1.split('|')
        data.append((word1[0],word1[1],word1[2],word1[3]))
       
    f.close()
    
    if request.method == 'POST':
        count = 0
        f = open('Record.txt', 'r')
        for l in f:
            l = l.split('|')
            if l[0] ==  id:
                count += 1

        if count >= 3:
            messages.warning(request,"Cannot Borrow more than 3 Books")
            return redirect('library-borrowbook')

        else:
            today = date.today()
            enddate = today+timedelta(days=7)
            bbook = request.POST.get('bbid')

            if len(str(bbook)) == 0:
                messages.warning(request,"You did not type anything")
                return redirect('library-borrowbook')

            pos = main.binary_search('Bindex.txt', bbook)
            if pos == -1:
                messages.warning(request,"The book that you had entered is not in our database,sorry,please enter a different book")
                return redirect('library-borrowbook')
            else:
                f2 = open('BData.txt', 'r+')
                f2.seek(pos)
                l2 = f2.readline()
                l2 = l2.rstrip('\n')
                w2 = l2.split('|')
                if(w2[3] == 'Y'):
                    l3 = w2[0] + '|' + w2[1] + '|' + w2[2] + '|' + 'N|#' 
                    f2.seek(pos)
                    f2.write(l3)
                    f2.close() 
                    messages.success(request,"The book you have selected has been successfully borrowed. Please return it by:" +'\n'+ str(enddate))

                    buf = id + '|' + bbook+ '|#\n'
                    f3 = open('Record.txt', 'a')
                    f3.write(buf)
                    f3.close()
                    main.key_sort('Record.txt')
                    return redirect('library-borrowbook')
                else:
                    messages.warning(request,"This book is currently unavailable, please select another book")
                    return redirect('library-borrowbook')



    else:
        return render(request, 'borrow.html',{"data":data,"headings":headings})

def returnbook(request):
    return render(request, 'return.html')