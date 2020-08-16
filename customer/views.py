from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from management.models import *
from .models import Reservation as ReservationModel
from .models import *
# Create your views here.

def Total(usr):
    Cartdish = Add_to_cart.objects.filter(user = usr)
    total = 0
    for i in Cartdish:
        total += i.dish.price * i.qty
    return Cartdish,total    

def Home(request):
    if request.user.is_staff:
        return redirect('AdminHome')
    else:    
        cat = Category.objects.all()
        dishes = Dish.objects.filter(available=True)
        special = todaySpecial.objects.all()
        if request.user.is_anonymous:
            d = {'cat':cat,'dishes':dishes,'special':special}
        else:
            Cartdish , total = Total(request.user)
            d = {'cat':cat,'dishes':dishes,'Cartdish':Cartdish,'total':total,'special':special}
        return render(request,'index.html',d)
    
def Contact(request):
    d={}
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('account')
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message'] 
        ContactUs.objects.create(name=name,email=email,subject=subject,message=message)   
    if request.user.is_authenticated:
        Cartdish , total = Total(request.user)
        d = {'Cartdish':Cartdish,'total':total}
    return render(request,'contact.html',d) 

def Reservation(request):
    d = {}
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('account')
        data = request.POST
        date = data['date']
        name = data['name']
        time = data['time']
        guests = data['guests']
        email = data['email']
        mob = data['mob']   
        ReservationModel.objects.create(user=request.user,mob=mob,name=name,email=email,guests=guests,time=time,date=date)
    if request.user.is_authenticated:
        Cartdish , total = Total(request.user)
        d = {'Cartdish':Cartdish,'total':total}
    return render(request,'reservation.html',d)   

def Account(request):
    errorLogin = False
    errorUser = False
    errorPass= False
    if 'login' in request.POST:
        un = request.POST['un']
        pwd = request.POST['pwd']   
        user = authenticate(username=un,password=pwd)
        if user:
            login(request,user)
            if request.user.is_staff:
                return redirect('AdminHome')
            else:   
                return redirect('home')    
        else:
            errorLogin = True
    if 'signup' in request.POST:
        e = request.POST['email']
        un = request.POST['un']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        check = User.objects.filter(username=un)
        if pwd1 != pwd2:      
            errorPass = True
        elif check:
            errorUser = True
        else:
           User.objects.create_user(username=un,email=e,password=pwd1,is_staff = False)
           user = authenticate(username=un,password=pwd1)
           login(request,user)  
           return redirect('home')         
    d = {'errorLogin':errorLogin,'errorPass':errorPass,'errorUser':errorUser}        
    return render(request,'account.html',d)  

def Logout(request):
    logout(request)
    return redirect('account')

def Cart(request):
    if request.user.is_authenticated:
        Cartdish , total = Total(request.user)
        d = {'Cartdish':Cartdish,'total':total}
    return render(request,'shop_cart.html',d)  

def DeleteOrder(request,Oid):
    Add_to_cart.objects.filter(id = Oid).delete()
    return redirect('cart')