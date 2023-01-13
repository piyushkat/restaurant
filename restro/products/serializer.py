from rest_framework import serializers
from products.models import *




class ProductSerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registratin Request
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'actual_price', 'quantity']


class GetProductSerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registratin Request
    class Meta:
        model = Product
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registratin Request
    class Meta:
        model = Category
        fields = ('name', 'image')
