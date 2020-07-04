from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from .models import Laptop,Adduser
from django.views import View
# from django.core.mail import send_mail
# from random import randint
from django.conf import settings

ec = ''
# Create your views here.
def login(request):
    if request.session.get('email'):
        return render(request,'index.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
    else:
        return render(request,'login.html',{'inout':'LOGIN','inoutl':'/account/login/'})

def afterlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        obj = Adduser.objects.get(email=email)
    except:
        error = "No such user...."
        return render(request,'login.html',{'inout':'LOGIN','inoutl':'/account/login/','error':error})
    else:
        if password == obj.password:
            request.session['email'] = email
            return render(request,'index.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
        else:
            error = "Invalid password"
            return render(request,'login.html',{'inout':'LOGIN','inoutl':'/account/login/','error':error})

def register(request):
    if request.session.get('email'):
        return render(request,'registration.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
    else:
        return render(request,'registration.html',{'inout':'LOGIN','inoutl':'/account/login/'})

class afterregister(View):
    def get(self,request):
        error = "Invalid method"
        if request.session.get('email'):
            return render(request,'registration.html',{'inout':'LOGOUT','inoutl':'/account/logout/','error':error})
        else:
            return render(request,'registration.html',{'inout':'LOGIN','inoutl':'/account/login/','error':error})
    
    def post(self,request):
        data = {
        'fname' : request.POST.get('fname'),
        'lname' : request.POST.get('lname'),
        'mobile' : request.POST.get('mobile'),
        'email' : request.POST.get('email'),
        'password' : request.POST.get('password'),
        }
        try:
            obje = Adduser.objects.get(email=data['email'])
            objm = Adduser.objects.get(email=data['mobile'])
        except Exception:   
            new_obj = Adduser.objects.create(**data)
            new_obj.save()
            if request.session.get('email'):
                return render(request,'index.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
            else:
                return render(request,'login.html',{'inout':'LOGIN','inoutl':'/account/login/'})
        else:
            error = "User already exists...."
            if request.session.get('email'):
                return render(request,'registration.html',{'inout':'LOGOUT','inoutl':'/account/logout/','error':error})
            else:
                return render(request,'registration.html',{'inout':'LOGIN','inoutl':'/account/login/','error':error})

def afterclick(request,sr):
    global ec
    email = request.session.get('email')
    obj = Adduser.objects.get(email=email)
    ec = obj.ecart
    if ec:ec = ec.split(',')
    else:ec = []
    ec.append(sr)
    ec = ','.join(ec)
    obj.ecart = ec
    obj.save()
    if request.session.get('email'):
        return render(request,'shopping-cart.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
    else:
        return render(request,'shopping-cart.html',{'inout':'LOGIN','inoutl':'/account/login/'})

def logout(request):
    del request.session['email']
    return render(request,'index.html',{'inout':'LOGIN','inoutl':'/account/login/'})

def importdata(request):
    with open('laptop.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            created = Laptop.objects.create(
            sr = row[0],
            company = row[1],
            name = row[2],
            rating = float(row[3]),
            no_rating = int(row[4]),
            mrp = int(row[5]),
            price = int(row[6]),
            less = int(row[7]),
            l1 = row[8],
            l2 = row[9],
            l3 = row[10],
            l4 = row[11],
            l5 = row[12],
            Screen_Size = row[13],
            Maximum_Display_Resolution = row[14],
            Item_Weight = row[15],
            Product_Dimensions = row[16],
            Batteries = row[17],
            Processor_Brand = row[18],
            Processor_Type = row[19],
            RAM_Size = row[20],
            Memory_Technology = row[21],
            Hard_Drive_Size = row[22],
            Hard_Disk_Technology = row[23],
            Graphics_Coprocessor = row[24],
            Operating_System = row[25],
            Date_First_Available = row[26]
            )
    if request.session.get('email'):
        return render(request,'index.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
    else:
        return render(request,'index.html',{'inout':'LOGIN','inoutl':'/account/login/'})

