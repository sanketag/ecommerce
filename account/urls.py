from django.urls import path
from .import views
# from .models import Cata

urlpatterns = [  
    path('login/',views.login),
    path('afterlogin/',views.afterlogin),
    path('register/',views.register),
    path('afterregister/',views.afterregister.as_view()),
    path('logout/',views.logout),
    path('importdata/',views.importdata),  
    path('<str:sr>/',views.afterclick),
]