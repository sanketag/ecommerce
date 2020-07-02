from django.urls import path
from .import views
# from .models import Cata

urlpatterns = [  
    path('about/',views.about),
    path('blog/',views.blog),
    path('cart/',views.cart),
    path('catalog/',views.catalog),
    path('contact/',views.contact),
    path('payment/',views.payment),
    path('<str:company>/<str:name>/',views.product),
    path('profile/',views.profile),
]