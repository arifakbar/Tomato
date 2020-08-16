from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    title = models.CharField(max_length=30,null=True,blank=True)
    des = models.TextField(null=True,blank=True)  
    img = models.FileField(null=True,blank=True)
    img1 = models.FileField(null=True,blank=True)
    img2 = models.FileField(null=True,blank=True)
    mrp = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    available = models.BooleanField(default=True,null=True,blank=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.title

class Team(models.Model):
    img = models.FileField(null=True,blank=True)
    name = models.CharField(max_length=20,null=True,blank=True)
    designation = models.CharField(max_length=20,null=True,blank=True)
    fb = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)  
    insta = models.URLField(null=True,blank=True)  

    def __str__(self):
        return self.name

class todaySpecial(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    img = models.FileField(null=True,blank=True)
    tagline =  models.TextField(null=True,blank=True)
    des = models.TextField(null=True,blank=True)  

    def __str__(self):
        return self.title  

        