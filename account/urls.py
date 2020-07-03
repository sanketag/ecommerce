from django.urls import path
from .import views
# from .models import Cata

urlpatterns = [  
    path('login/',views.login),
    path('afterlogin/',views.afterlogin),
    path('register/',views.register),
    path('afterregister/',views.afterregister.as_view()),
    path('logout/',views.logout),
    path('<str:name>/',views.afterclick),
    path('importdata/',views.importdata),  
]