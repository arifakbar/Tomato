from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('contact/',Contact,name='contact'),
    path('account/',Account,name='account'),
    path('reservation/',Reservation,name='reservation'),
    path('logout/',Logout,name='logout'),
    path('cart/',Cart,name="cart"),
    path("delete-order/<int:Oid>/", DeleteOrder, name="DeleteOrder")    
]