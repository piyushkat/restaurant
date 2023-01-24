from rest_framework import serializers
from meal_req.models import *
from food.models import *



class RequestMedicineSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(many=True, queryset=Cartitems.objects.all())

    class Meta:
        model = RequestMedicine
        fields = ('user', 'phone_no', 'address', 'latitude', 'longitude', 'date', 'cart')


class UpdateUserDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = RequestMedicine
    fields = ['phone_no','address','latitude','longitude']



class OrderStatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderStatus
    fields = ['medicine','store_info','status']


class StoreInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = StoreInfo
    fields = ['name','address','latitude','longitude','owner']


class DeliveryBoySerializer(serializers.ModelSerializer):
  medicine = RequestMedicineSerializer(read_only = True)
  class Meta:
    model = DeliveryBoy
    fields = ['user','order','date','medicine']
