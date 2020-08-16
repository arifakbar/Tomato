from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('about/',About,name='about'),
    path('menu/',Menu,name='menu'),
    path('shop/<int:dishid>/',Shop,name="shop"),
    path('AdminHome/',AdminHome,name='AdminHome'),
    path('editCat/',EditCategory,name="editCat"),
    path('editDish/',EditDish,name='editDish'),
    path('editTeam/',EditTeam,name='editTeam'),
    path('contactUs/',ContactMsg,name='contactUs')
]