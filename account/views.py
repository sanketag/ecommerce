from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Laptop

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'registration.html')

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
