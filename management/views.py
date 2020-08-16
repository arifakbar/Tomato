from django.shortcuts import render,redirect
from management.models import *
from customer.models import Add_to_cart
from customer.views import *
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# Create your views here.
def About(request):
    members = Team.objects.all()
    d={'members':members}
    if request.user.is_authenticated:
        Cartdish , total = Total(request.user)
        d = {'members':members,'Cartdish':Cartdish,'total':total}
    return render(request,'about.html',d)

def Menu(request):
    cat = Category.objects.all()
    dishes = Dish.objects.filter(available=True)
    d = {'cat':cat,'dishes':dishes}
    if request.user.is_authenticated:
        Cartdish , total = Total(request.user)
        d = {'cat':cat,'dishes':dishes,'Cartdish':Cartdish,'total':total}
    return render(request,'menu_all.html',d)

    

def Shop(request, dishid):
    dish = Dish.objects.filter(id = dishid).first()
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('account')
        qty = request.POST['qty']
        data = Add_to_cart.objects.filter(user = request.user, dish = dish).first()
        if data:
            Add_to_cart.objects.filter(user = request.user, dish = dish).update(qty=qty)
        else:
            Add_to_cart.objects.create(user = request.user, dish = dish,qty=qty)
    d = {'dish':dish}
    if request.user.is_authenticated:
        Cartdish , total = Total(request.user)
        d = {'dish':dish,'Cartdish':Cartdish,'total':total}
    return render(request, 'shop.html',d)  

def Cart(request):
    orders, total = Total(request.user)
    d = {'orders':orders, 'total':total}
    return render(request, 'shop_cart.html',d)            

def AdminHome(request):
    if request.user.is_anonymous:
        return redirect('account')
    if not request.user.is_staff:
        return redirect('home')
    res = ReservationModel.objects.all()
    order = Add_to_cart.objects.all()
    if "confirm" in request.POST:
        ReservationModel.objects.filter(id = request.POST['confirm']).update(confirm=True)
        r = ReservationModel.objects.get(id = request.POST['confirm'])
        sub = "Reservation confirmed at Tomato"
        from_mail = settings.EMAIL_HOST_USER
        data = {'name':r.name,'guests':r.guests,'date':r.date,'time':r.time}
        html = get_template('mail.html').render(data)
        msg = EmailMultiAlternatives(sub,'',from_mail,[r.email])
        msg.attach_alternative(html,'text/html')
        print('result = ', msg.send())
    if 'cancel' in request.POST:
        r = ReservationModel.objects.get(id = request.POST['cancel'])
        sub = "Reservation coudn't be confirmed at Tomato"
        from_mail = settings.EMAIL_HOST_USER
        data = {'name':r.name,'guests':r.guests,'date':r.date,'time':r.time}
        ReservationModel.objects.get(id = request.POST['cancel']).delete() 
        html = get_template('cancelMail.html').render(data) 
        msg = EmailMultiAlternatives(sub,'',from_mail,[r.email])
        msg.attach_alternative(html,'text/html')
        print('result = ', msg.send())
    if 'confirmOrder' in request.POST:
        Add_to_cart.objects.filter(id = request.POST['confirmOrder']).update(confirmation = True)          
    if 'cancelOrder' in request.POST:
        Add_to_cart.objects.get(id = request.POST['cancelOrder']).delete()  
    d = {'res':res , 'order':order}         
    return render(request,'index2.html',d)

def EditCategory(request):
    cat = Category.objects.all()
    if 'delete' in request.POST:
        Category.objects.get(id = request.POST['delete']).delete()  
    d = {'cat':cat}
    if 'addCat' in request.POST:
        Category.objects.create(name = request.POST['catName'])
    return render(request,'editCat.html',d)

def EditDish(request):
    cat = Category.objects.all()
    dish = Dish.objects.all()

    if 'unavail' in request.POST:
        Dish.objects.filter(id = request.POST['unavail']).update(available=False)

    if 'avail' in request.POST:
        Dish.objects.filter(id = request.POST['avail']).update(available=True)   

    if 'add' in request.POST:
        category = Category.objects.get(id = request.POST['category'])
        title = request.POST['title']
        des = request.POST['des']    
        price = request.POST['price']    
        mrp = request.POST['mrp']    
        img = request.FILES['img']    
        img1 = request.FILES['img1']    
        img2 = request.FILES['img2']    
        Dish.objects.create(cat = category , title=title, des=des, price=price, mrp=mrp, img=img, img1=img1, img2=img2)

    if 'delete' in request.POST:
        Dish.objects.get(id = request.POST['delete']).delete()      

    d={'cat':cat,'dish':dish}
    return render(request,'editDish.html',d)

def EditTeam(request):
    team = Team.objects.all()
    if 'add' in request.POST:
        name = request.POST['name']
        designation = request.POST['designation']
        fb = request.POST['fb']
        insta = request.POST['insta']
        twitter = request.POST['twitter']
        img = request.FILES['img']
        Team.objects.create(name=name,designation=designation,fb=fb,insta=insta,twitter=twitter,img=img)

    if 'delete' in request.POST:
        Team.objects.get(id = request.POST['delete']).delete()  

    d = {'team':team}
    return render(request,'editTeam.html',d)    

def ContactMsg(request):
    contactmsg = ContactUs.objects.all()
    d = {'contactmsg':contactmsg}
    if 'delete' in request.POST:
        ContactUs.objects.get(id = request.POST['delete']).delete()   
    return render(request,'contactUs.html',d)    