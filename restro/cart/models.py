from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cartitems(models.Model):
    product = models.ManyToManyField(Product,related_name = 'product_id',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)