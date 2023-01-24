from django.db import models
from django.contrib.auth.models import User
from cart.models import Cartitems

# Create your models here.
class RequestMedicine(models.Model):
    cart = models.ManyToManyField(Cartitems,related_name='cart_id')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=500)
    latitude = models.DecimalField(decimal_places=5, max_digits=7)
    longitude = models.DecimalField(decimal_places=5,max_digits=7)
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
    ("order_not_accepted","order_not_accepted"),
    ("order_accepted","order_accepted"),
    ("order_packed","order_packed"),  
    ("order_picked","order_picked"),
    ("on_the_way","on_the_way"),
    ("delivered","delivered"),
)


# found,not_found,partially_found
class OrderStatus(models.Model):
    cart  = models.ManyToManyField(RequestMedicine,related_name='cart_id')
    store_info = models.ForeignKey(StoreInfo,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)  
    status = models.CharField(max_length=100,choices=status,default="waiting_for_confirmation")


class DeliveryBoy(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ManyToManyField(RequestMedicine,related_name='order_id')
    date = models.DateTimeField(auto_now=True)