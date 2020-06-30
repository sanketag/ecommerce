from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request,'about-us.html')

def blog(request):
    return render(request,'blog-post-list.html')

def cart(request):
    return render(request,'shopping-cart.html')

def catalog(request):
    return render(request,'catalog-page.html')

def contact(request):
    return render(request,'contact-us.html')

def payment(request):
    return render(request,'payment-page.html')

def product(request):
    return render(request,'product-page.html')

def profile(request):
    return render(request,'profile.html')
