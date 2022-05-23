from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class seller_Profiles(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE )
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    tel_no = models.CharField(max_length=10,null=True)
    seller = models.BooleanField(default=False)
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile/')


    def __str__(self) :
        return str(self.user)


class Houses(models.Model):
   apartment_name = models.CharField(max_length=10)
   apartment_img1 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
   apartment_owner = models.ForeignKey(seller_Profiles,on_delete=models.CASCADE,null=True)
   apartment_img2 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
   apartment_img3 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
   apartment_img4 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
   apartment_img5 = models.ImageField(null=True,blank=True,upload_to='images/apartments/')
   apartment_location   = models.TextField(null=True)
   apartment_price   = models.IntegerField(null=True)
   apartment_describ = models.TextField(null=True)
   rent_period =  models.TextField(null=True)
   book = models.BooleanField(default=False)

   def __str__(self) :
       return self.apartment_name
    
   def get_absolute_url(self):
       return reverse("home",args=None)




    



         