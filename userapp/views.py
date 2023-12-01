from django.shortcuts import render,redirect
import pkg_resources
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
      return render(request,'home.html')
def login(request):
      if request.method=="POST":
            try:
                  email=request.POST.get("email")
                  password=request.POST.get("password")
                  login=user_reg.objects.get(Email=email,Password=password)
                  request.session['Email']=login.Email
                  request.session['id']=login.id
                  return redirect("home")
            except user_reg.DoesNotExist as e:
                  messages.info(request,'invalid email/password')
      return render(request,'login.html')

def reg(request):
      if request.method=="POST":
            name=request.POST.get("name")
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            password=request.POST.get("password")
            cpassword=request.POST.get("cpassword")
            if  password==cpassword:
                  if user_reg.objects.filter (Email=email).exists():
                        messages. info(request, 'Email already exists')
                  elif user_reg.objects.filter(Phone=phone).exists():
                        messages. info(request, 'phonenumber already exists')
                  else:
                        userdata=user_reg(Name=name,Email=email,Phone=phone,Password=password)
                        userdata.save()
                        return redirect("login")
            else:
               messages.info(request, 'password not match')
      return render(request,'reg.html')