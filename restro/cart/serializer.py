from rest_framework import serializers
from django.contrib.auth.models import User
from cart.models import Cartitems
from products.serializer import ProductSerializer



class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['id','product_id','quantity']


class ViewCartSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Cartitems
        fields = ['id','product','quantity']


class DeleteCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['id']