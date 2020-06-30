from django.urls import path
from .import views
# from .models import Cata

urlpatterns = [  
    path('login/',views.login),
    path('register/',views.register),
    path('importdata/',views.importdata),  
]