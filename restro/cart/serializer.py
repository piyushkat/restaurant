from rest_framework import serializers
from django.contrib.auth.models import User
from cart.models import Cartitems



class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['id','product_id','quantity']


class ViewCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['id','product_id','quantity']


class DeleteCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['id']