from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.session.get('email'):
        return render(request,'index.html',{'inout':'LOGOUT','inoutl':'/account/logout/'})
    else:
        return render(request,'index.html',{'inout':'LOGIN','inoutl':'/account/login/'})

