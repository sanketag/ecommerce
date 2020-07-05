from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models import Laptop,Adduser

# Create your views here.
def about(request):
    if request.session.get('email'):
        return render(request,'about-us.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
    else:
        return render(request,'about-us.html',{'inout':'LOGIN','inoutl':'/account/login/'})

def blog(request):
    if request.session.get('email'):
        return render(request,'blog-post-list.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
    else:
        return render(request,'blog-post-list.html',{'inout':'LOGIN','inoutl':'/account/login/'})

def cart(request):
    price = 0
    l = []
    if request.session.get('email'):
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
        return render(request,'shopping-cart.html',{'inout':'LOGOUT','inoutl':'/account/logout/','l':l,'price':price})
    else:
        return render(request,'shopping-cart copy.html',{'inout':'LOGIN','inoutl':'/account/login/'})

def catalog(request):
    prod = Laptop.objects.all()
    prod=list(prod)
    if request.session.get('email'):
        return render(request,'catalog-page.html',{'inout':'LOGOUT','inoutl':'/account/logout/','allProds':prod})
    else:
        return render(request,'catalog-page.html',{'inout':'LOGIN','inoutl':'/account/login/','allProds':prod})

def contact(request):
    if request.session.get('email'):
        return render(request,'contact-us.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
    else:
        return render(request,'contact-us.html',{'inout':'LOGIN','inoutl':'/account/login/'})

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
    params = {'l':l,'price':price,'inout':'LOGOUT','inoutl':'/account/logout/'}
    return render(request,'payment-page.html',params)

def product(request,name):
    model = Laptop.objects.filter(name=name)
    prod = Laptop.objects.all()
    prod=list(prod)
    if request.session.get('email'):
        return render(request,'product-page.html',{'inout':'LOGOUT','inoutl':'/account/logout/','allProds':model,'all':prod})
    else:
        return render(request,'product-page.html',{'inout':'LOGIN','inoutl':'/account/login/','allProds':model,'all':prod})

def search(request):
    query = request.GET['search']
    if len(query)>208:
        allProds = Laptop.objects.none()

    else:
        allPostsCompany=Laptop.objects.filter(company__icontains=query)
        allPostsName=Laptop.objects.filter(name__icontains=query)
        allProds= allPostsCompany.union(allPostsName)

    # if allPosts.count() == 0:
    #     messages.warning(request,"No search results found.Please refine your query")
    if request.session.get('email'):
        return render(request,'catalog-page.html',{'inout':'LOGOUT','inoutl':'/account/logout/','allProds':allProds})
    else:
        return render(request,'catalog-page.html',{'inout':'LOGIN','inoutl':'/account/login/','allProds':prod})
    
        

# def profile(request):
#     if request.session.get('email'):
#         return render(request,'profile.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
#     else:
#         return render(request,'profile.html',{'inout':'LOGIN','inoutl':'/account/login/'})

