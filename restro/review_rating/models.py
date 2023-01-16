from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

ratings_level = (
    (0,0),
    (1,1),
    (1.5,1.5),
    (2,2),
    (2.5,2.5),
    (3,3),
    (3.5,3.5),
    (4,4),
    (4.5,4.5),
    (5,5),
)   


class ReviewRating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    products = models.ForeignKey(Product,on_delete=models.CASCADE,default=True) 
    review = models.TextField(max_length=554,null=True)
    ratings = models.IntegerField(choices=ratings_level, default=None)
    created_at = models.DateTimeField(auto_now=True)
