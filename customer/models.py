from django.db import models
from django.contrib.auth.models import User
from management.models import Dish
# Create your models here.
class Add_to_cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True, default=1)
    confirmation = models.BooleanField(blank=True, null=True, default=False)
    
    def __str__(self):
        return self.dish.title


class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(blank=True,null=True,max_length=20)
    email = models.CharField(blank=True,null=True,max_length=40)
    guests = models.IntegerField(blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    time = models.TimeField(blank=True,null=True)
    confirm = models.BooleanField(blank=True,null=True,default=False)
    mob = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.name + '---' + str(self.date) + '---' + str(self.time)

class ContactUs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)            
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name