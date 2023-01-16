from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RequestMedicine(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/medicine')
    phone_no = models.IntegerField()
    address = models.TextField(max_length=500)
    latitude = models.DecimalField(decimal_places=5, max_digits=7)
    longitude = models.DecimalField(decimal_places=5,max_digits=7)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class StoreInfo(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    latitude = models.DecimalField(max_digits=7,decimal_places=5)
    longitude = models.DecimalField(max_digits=7,decimal_places=5)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


status = (
    ("waiting_for_confirmation","waiting_for_confirmation"),
    ("partially_found","partially_found"),
    ("not_accepted_order","not_accepted_order"),
    ("order_accepted","order_accepted"),
    ("order_packed","order_packed"),  
    ("order_picked","order_picked"),
    ("on_the_way","on_the_way"),
    ("delivered","delivered"),
)


# found,not_found,partially_found
class OrderStatus(models.Model):
    medicine  = models.ForeignKey(RequestMedicine,on_delete=models.CASCADE)
    store_info = models.ForeignKey(StoreInfo,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)  
    status = models.CharField(max_length=100,choices=status,default="waiting_for_confirmation")