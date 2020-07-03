from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models import Laptop,Adduser
# Create your views here.
def about(request):
    return render(request,'about-us.html')

def blog(request):
    return render(request,'blog-post-list.html')

def cart(request):
    email = request.session.get('email')
    obj = Adduser.objects.get(email=email)
    ec = obj.ecart
    if ec:ec = ec.split('@')
    else:ec = []
    prod = Laptop.objects.all()
    prod=list(prod)
    print(ec)
    print(prod)
    params = {'ec':ec,'all':prod}
    return render(request,'shopping-cart.html')

def catalog(request):
    prod = Laptop.objects.all()
    prod=list(prod)
    params = {'allProds':prod}
    return render(request,'catalog-page.html',params)

def contact(request):
    return render(request,'contact-us.html')

def payment(request):
    return render(request,'payment-page.html')

def product(request,name):
    model = Laptop.objects.filter(name=name)
    prod = Laptop.objects.all()
    prod=list(prod)
    params = {'allProds':model,'all':prod}
    return render(request,'product-page.html',params)

def profile(request):
    return render(request,'profile.html')

