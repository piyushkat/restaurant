from django.shortcuts import render
import datetime
import environ
from rest_framework.response import Response
from rest_framework import status
from food.serializer import *
from rest_framework.generics import GenericAPIView
from food.renderers import UserRenderer
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.permissions import IsAuthenticated
from food.helper import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import datetime, timedelta
from meal_req.models import *
from meal_req.serializer import *
from collections import OrderedDict


# Create your views here.
class DeliveryProcess(GenericAPIView):
  serializer_class = RequestMedicineSerializer
  renderer_classes = [UserRenderer]
  def post(self,request):
    """
    :return: Request medicine by the user and find the nearest store.
    """
    try:
      if not self.request.user.is_authenticated:
        return Response({'msg':'user not found'})
      # Request medicine by the user to the request medicine table
      serializer = RequestMedicineSerializer(data=request.data)
      # if the json data is valid.
      serializer.is_valid(raise_exception=True)
      # update the table
      serializer.save()
      # Find the distance from user to the store  
      start_x = float(request.data.get('latitude'))
      start_y= float(request.data.get('longitude'))
      # get all the store info
      res = StoreInfo.objects.all().values()
      dict = {}
      for i in range(len(res)):
        # distance to the store from the User
        end_x = float(res[i]["latitude"])
        end_y = float(res[i]["longitude"])
        distance = get_distance(start_x,start_y,end_x,end_y)
        # stored  the distance of the user in a dictionary 
        # with key as distance and value as store to which distance is calculated
        dict[distance] = res[i]
      # sort the items in the order dict table 
      dict1 = OrderedDict(sorted(dict.items()))
      sorted_items=list(dict1.values())[0]
      # get the store info id
      store = StoreInfo.objects.get(id=sorted_items['id'])
      # create the order by the user to request the medicine byt he request medicine table
      order = OrderStatus.objects.create(medicine=RequestMedicine.objects.get(name=request.data.get('name')),store_info=store ) # validate name
      # convert data into json format
      serializer = OrderStatusSerializer(OrderStatus.objects.filter(store_info=store),many=True)
      return Response({"status": "success", "data": serializer.data}, status= 200)
    except:
      return Response ({"status": "Already order placed"}, status=203)


class MedicineOrderApporve(GenericAPIView):
  serializer_class = RequestMedicineSerializer
  renderer_classes = [UserRenderer]
  def post(self,request,id):
    """
    :return: Approve the order by pharmacy.
    """
    try:
      if not self.request.user.is_authenticated:
        return Response({"msg":"No user Found"})
        # Request the user to have permission to change the order status.
      if self.request.user.has_perm('firstapp.change_orderstatus'):
        # Get the order id in the order status table.
        order = OrderStatus.objects.filter(id=id).values('store_info')
        owner = StoreInfo.objects.filter(id=order[0]['store_info']).values('owner')
        if owner[0]['owner'] == self.request.user.id:  
          order = OrderStatus.objects.get(id=id)
          # order Accepted 
          order.status= "order_accepted"
          # order status table updated when the pharmacy accepted the order. 
          # converted the data into json.
          order.save()
          serializer = OrderStatusSerializer(OrderStatus.objects.filter(id=id),many=True)
          return Response({"status": "Success", "data": serializer.data}, status=200)
        return Response({"status": "You are not authorized"}, status=203)
      return Response({"status": "You are not authorized"}, status=203)
    except:
      return Response ({"status": "Invalid Address"}, status=203)


def NextStore(self,request,id):
  """
  :return: The next phamacy nearest to the user
  """
  order = OrderStatus.objects.filter(id=id).values('store_info')
  owner = StoreInfo.objects.filter(id=order[0]['store_info']).values('owner')
  if owner[0]['owner'] == self.request.user.id:    
    # Get the order that was refused by pharmacy
    order =OrderStatus.objects.filter(id=id).values()
    # Medicine requested bt the user
    medicine_value = RequestMedicine.objects.filter(id=order[0]['medicine_id']).values() # and user id
    # getting the latitude and longitude of user location
    start1 = medicine_value[0]['latitude']
    start2 = medicine_value[0]['longitude']
    # get all the stores from database(for poc only,afterwards will filter within the radius of user
    res = StoreInfo.objects.all().values()
    dict = {}
    for i in range(len(res)):
      # distance of store from the user in km 
      end1 = float(res[i]["latitude"])
      end2 = float(res[i]["longitude"])
      distance = get_distance(start1,start2,end1,end2)
      # stored  the distance of the user in a dictionary 
      # with key as distance and value as store to which distance is calculated
      dict[distance] = res[i]
    # sorted the dictionary according to distance(key in dict)
    dict1 = OrderedDict(sorted(dict.items()))
    # get the store that refused the order
    store = StoreInfo.objects.filter(id=order[0]['store_info_id']).values()
    # get index of the store that refused the medicine in sorted dictionary
    index = list(dict1.values()).index(store[0])
    # if the index is more than the stores available in database 
    if index+1>=len(list(dict1.values())):
      order = OrderStatus.objects.get(id=id)
      order.status = 'not_found'
      order.save()
      return  Response({"status": "Not available"},status=204)
    # get the next store available in the sorted dict
    next_store=list(dict1.values())[index+1]
    # created the instance of the next nearest store to the user 
    res = StoreInfo.objects.get(id=next_store['id'])
    order = OrderStatus.objects.get(id=id)
    order.store_info = res
    # Updated the order with the next nearest store after the order is refused
    order.save()
    return res


class PartiallyFoundMedicine(GenericAPIView):
  serializer_class = RequestMedicineSerializer
  renderer_classes = [UserRenderer]
  def post(self,request,id):
    if not self.request.user.is_authenticated:
      return Response({"msg":"No user Found"})
    if self.request.user.has_perm('firstapp.change_orderstatus'):
      res = NextStore(self,request,id)
      order = OrderStatus.objects.get(id=id)
      order.status = "partially_found"
      order.save()
      serializer = OrderStatusSerializer(order)
      return Response({"status": "success", "data": serializer.data}, status=200)
    return Response({"status": "You are not Authorized"}, status=200)
    

class MedicineOrderDecline(GenericAPIView):
  serializer_class = RequestMedicineSerializer
  renderer_classes = [UserRenderer]
  def post(self,request,id):
    """
    :return: To decline the order of medicine ordered by the customer.
    """
    if not self.request.user.is_authenticated:
      # chck the user is authenticated or not.
      return Response({"msg":"No user Found"})
    if self.request.user.has_perm('firstapp.change_orderstatus'):
      # check if the user has parameter to decline the order
      res = NextStore(self,request,id)
        # converted the data into json format
      serializer = OrderStatusSerializer(OrderStatus.objects.all(),many=True)
      # get all the fields of the user
      return Response({'msg':"success","data":serializer.data},status=200)
    return Response({"status": "You are not authorized"}, status=203)


class MedicineRequestPerStore(GenericAPIView):
  serializer_class = RequestMedicineSerializer
  renderer_classes = [UserRenderer]
  def get(self,request):
    if self.request.user.is_authenticated:
      # check the user is logged in or not.
      StoreId = StoreInfo.objects.filter(owner=self.request.user.id).values('id')
      # Get the store id of the user
      orders_per_store = OrderStatus.objects.filter(store_info=StoreId[0]['id']).values('id','medicine')
      # check the orders of all the stores
      medicine_detail = RequestMedicine.objects.filter(id=orders_per_store[0]['medicine'])
      # filter the medical details.
      serializer = RequestMedicineSerializer(medicine_detail,many=True)
      return Response({"status": "success", "data": serializer.data}, status=200)
    return Response({"status": "Login Required"}, status=407)

