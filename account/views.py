from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Laptop,Adduser
from internal.models import Addcart
from django.views import View
# from django.core.mail import send_mail
# from random import randint
from django.conf import settings

# Create your views here.
def login(request):
    if request.session.get('email'):
        return render(request,"index.html")
    else:
        return render(request,'login.html')

def afterlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email,password)
    try:
        obj = Adduser.objects.filter(password=password)
        print(obj)
    except:
        error = "No such user...."
        return render(request,"login.html",{'error':error})
    else:
        if password == obj.password:
            # request.session['email'] = email
            return render(request,"index.html")
        else:
            error = "Invalid password"
            return render(request,"login.html",{'error':error})

def register(request):
    return render(request,'registration.html')

class afterregister(View):
    def get(self,request):
        error = "Invalid method"
        return render(request,'registration.html')
    
    def post(self,request):
        data = {
        'fname' : request.POST.get('fname'),
        'lname' : request.POST.get('lname'),
        'mobile' : request.POST.get('mobile'),
        'email' : request.POST.get('email'),
        'password' : request.POST.get('password'),
        }
        em = {
        'email' : request.POST.get('email'),
        }
        try:
            obje = Adduser.objects.get(email=data['email'])
            objm = Adduser.objects.get(email=data['mobile'])
        except Exception:   
            new_obj = Adduser.objects.create(**data)
            new_obj.save()
            new_ob = Addcart.objects.create(**em)
            new_ob.save()
            return render(request,"index.html")
        else:
            error = "User already exists...."
            return render(request,"register.html",{'error':error})

def logout(request):
    del request.session['email']
    return redirect('/account/login/')

def importdata(request):
    with open('laptop.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            created = Laptop.objects.create(
            company = row[0],
            name = row[1],
            rating = float(row[2]),
            no_rating = int(row[3]),
            mrp = int(row[4]),
            price = int(row[5]),
            less = int(row[6]),
            l1 = row[7],
            l2 = row[8],
            l3 = row[9],
            l4 = row[10],
            l5 = row[11],
            Screen_Size = row[12],
            Maximum_Display_Resolution = row[13],
            Item_Weight = row[14],
            Product_Dimensions = row[15],
            Batteries = row[16],
            Processor_Brand = row[17],
            Processor_Type = row[18],
            RAM_Size = row[19],
            Memory_Technology = row[20],
            Hard_Drive_Size = row[21],
            Hard_Disk_Technology = row[22],
            Graphics_Coprocessor = row[23],
            Operating_System = row[24],
            Date_First_Available = row[25]
            )
    return HttpResponse("success")




















    # l name,price
    # l.append(name,price)
    # l