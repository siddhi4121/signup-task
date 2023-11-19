from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def SignupPage(request):
    if request.method=='post':
        uname=request.POST.get('username')
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User.object.create_user(uname,fname,lname,email,password)
        my_user.save()
        return HttpResponse("User has been created sucessfully!!!")
        print(uname,fname,lname,email,password)

    return render (request,'signup.html')

def LoginPage(request):
    return render (request,'login.html')