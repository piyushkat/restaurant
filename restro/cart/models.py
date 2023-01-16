from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cartitems(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s %s'%(self.quantity, self.product.name)