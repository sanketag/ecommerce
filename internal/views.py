from django.shortcuts import render
from django.http import HttpResponse
from account.models import Laptop
from .models import Addcart
# Create your views here.
def about(request):
    return render(request,'about-us.html')

def blog(request):
    return render(request,'blog-post-list.html')

def cart(request):
    return render(request,'shopping-cart.html')

def catalog(request):
    prod = Laptop.objects.all()
    prod=list(prod)
    params = {'allProds':prod}
    print(params)
    return render(request,'catalog-page.html',params)

def contact(request):
    return render(request,'contact-us.html')

def payment(request):
    return render(request,'payment-page.html')

def product(request,company,name):
    model = Laptop.objects.filter(name=name)
    prod = Laptop.objects.all()
    prod=list(prod)
    params = {'allProds':model,'all':prod}
    return render(request,'product-page.html',params)

def profile(request):
    return render(request,'profile.html')
