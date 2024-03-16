from django.db import models

import os
import datetime

# Create your models here.
class shopping(models.Model):
    pass

def getFilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads',new_filename)

class category(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='image/',null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table="category"

class subcategory(models.Model):
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='image/',null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table="subcategory"

class product(models.Model):
    subcategory= models.ForeignKey(subcategory, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    detail= models.TextField()
    quantity= models.IntegerField()
    image= models.ImageField(upload_to='image/',null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="product"

class register(models.Model):
    Name=models.CharField(max_length=20,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)
    Retypepass=models.CharField(max_length=20,null=True,blank=True)
    Phnumber=models.IntegerField(blank=True,null=True)
    
    class Meta:
        db_table="register"

class cart(models.Model):
    product= models.ForeignKey(product, on_delete=models.CASCADE)
    register= models.ForeignKey(register, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    detail= models.TextField()
    quantity= models.IntegerField()
    image= models.ImageField(upload_to='image/',null=True,blank=True)
    totalprice= models.IntegerField()

    class Meta:
        db_table="cart"

class order(models.Model):
    product= models.ForeignKey(product, on_delete=models.CASCADE)
    register= models.ForeignKey(register, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    detail= models.TextField()
    quantity= models.IntegerField()
    image= models.ImageField(upload_to='image/',null=True,blank=True)
    totalprice= models.IntegerField()
    conformation=models.BooleanField(default=False)
    delivery=models.CharField(max_length=50)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        db_table="order"



