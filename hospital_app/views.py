from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    doctordata = DoctorProfile.objects.all()
    patientdata = PatientProfile.objects.all()
    msg = "Dear, Welcome To Stazi"    
    return render(request,'index.html',{ 'text': msg})


#To Register
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email_id = request.POST['email']
        password = request.POST['Password1']
        confirm_password = request.POST['Password2']
        phone = request.POST['phone']
        profile_pic = request.FILES.get('profile_img')
        user_type = request.POST.get('user-type')
        print(user_type)
        # data={
        #     'first_name' : request.POST['first_name'],
        #     'last_name' : request.POST['last_name'],
        #     'username' : request.POST['username'],
        #     'email' : request.POST['email'],
        #     'password' : request.POST['Password1'],
        # }
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already exists')
                return redirect('/register')
            elif User.objects.filter(email = email_id).exists():
                messages.info(request,'Email already exists')
                return redirect('/login')
            else:
                user = User.objects.create_user(username=username,email=email_id,password=password,first_name=first_name,last_name=last_name)
                #user = User.objects.create_user(**data)
                user.save()
                if user_type == "doctor":
                    doctordata=DoctorProfile.objects.create(name=username,email_id=email_id,profile_photo=profile_pic,user_id=user.id)
                    doctordata.save()
                else:
                    patientdata=PatientProfile.objects.create(name=username,email_id=email_id,profile_photo = profile_pic,user_id=user.id)
                    patientdata.save()
                return redirect('/login')
        else:
            messages.info(request,'Password doesnot matching')
            return redirect('/register')
    
    else:
        return render(request,'register.html')

# To login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        Password = request.POST.get('password')
        print(request,username,Password)
        user = authenticate(request, username=username,password=Password)
        #print(user) 
        if user is not None:
            print("login")
            messages.info(request,'login sucssfully')
            auth.login(request,user)
            #print('login sucssfully')
            #return index(request)
            return displayview(request,user.username)
        else:
            messages.info(request,'user not found')
            print("logout")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

# To logout  
def logout(request):
    auth.logout(request)
    return redirect('/')

#dashboarda
def displayview(request,user):
    msg = f"Dear {user}, Welcome To Stazi"
    doctor=DoctorProfile.objects.all() 
    patient = PatientProfile.objects.all()
    #print(doctor,patient)
    for i in doctor:
        if user == i.name:
            return render(request,'index.html',{'text':msg,'doctor':doctor})
    return render(request,'index.html',{'text':msg,'patient':patient})

    