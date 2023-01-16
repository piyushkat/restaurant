from rest_framework import serializers
from meal_req.models import *
from food.models import *


class RequestMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestMedicine
        fields = ('name', 'image', 'phone_no', 'address',
                   'latitude', 'longitude', 'user')


class OrderStatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderStatus
    fields = ['medicine','store_info','status']


class StoreInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = StoreInfo
    fields = ['name','address','latitude','longitude','owner']
