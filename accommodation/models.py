
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
# Create your models here.
class seller_Profile(models.Model):
    #user = models.OneToOneField(User,null=True,on_delete=models.CASCADE )
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    tel_no = models.CharField(max_length=10,null=True)

    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile/')


    def __str__(self) :
        return str(self.user)

class customer(models.Model):
    customer_user = models.OneToOneField(User,null=True,on_delete=models.CASCADE )
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/CustomerProfile/')

    def __str__(self):
        return str(self.customer_user)

class Apartment(models.Model):
    apartment_name = models.CharField(max_length=255)
    apartment_owner = models.ForeignKey(seller_Profile,on_delete=models.CASCADE,null=True) 
    customer = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    apartment_img1 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
    apartment_img2 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
    apartment_img3 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
    apartment_img4 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
    apartment_location   = models.TextField()
    apartment_price   = models.IntegerField()
    apartment_describ = models.TextField()
    book = models.BooleanField(default=False)

    def __str__(self) :
        return self.apartment_name 

    def get_absolute_url(self):
        return reverse("home",args=None)

class Booking_details(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    customer = models.OneToOneField(User,null=True,on_delete=models.CASCADE )
    apartment = models.ForeignKey(Apartment,null=True,on_delete=models.CASCADE )
    tel_no = models.CharField(max_length=10)
    occupation = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.customer)

class Home(models.Model):
   tel_no = models.CharField(max_length=10) 
    
