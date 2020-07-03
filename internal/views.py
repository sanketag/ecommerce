from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models import Laptop,Adduser

# Create your views here.
def about(request):
    return render(request,'about-us.html')

def blog(request):
    return render(request,'blog-post-list.html')

def cart(request):
    price = 0
    l = []
    email = request.session.get('email')
    obj = Adduser.objects.get(email=email)
    prod = Laptop.objects.all()
    prod=list(prod)
    ec = obj.ecart
    if ec:ec = list(map(int,ec.split(',')))
    else:ec = []
    for i in ec:
        l.append([prod[i].name,prod[i].price,prod[i].l1])
        price += prod[i].price
    params = {'l':l,'price':price}
    return render(request,'shopping-cart.html',params)

def catalog(request):
    prod = Laptop.objects.all()
    prod=list(prod)
    params = {'allProds':prod}
    return render(request,'catalog-page.html',params)

def contact(request):
    return render(request,'contact-us.html')

def payment(request):
    price = 0
    l = []
    email = request.session.get('email')
    obj = Adduser.objects.get(email=email)
    prod = Laptop.objects.all()
    prod=list(prod)
    ec = obj.ecart
    if ec:ec = list(map(int,ec.split(',')))
    else:ec = []
    for i in ec:
        l.append([prod[i].name,prod[i].price,i+1])
        price += prod[i].price
    params = {'l':l,'price':price}
    return render(request,'payment-page.html',params)

def product(request,name):
    model = Laptop.objects.filter(name=name)
    prod = Laptop.objects.all()
    prod=list(prod)
    params = {'allProds':model,'all':prod}
    return render(request,'product-page.html',params)

def profile(request):
    return render(request,'profile.html')

