from django.shortcuts import render
from products.models import *
from food.renderers import UserRenderer
from products.serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from products.helper import *
# Create your views here.


class GetAllProduct(GenericAPIView):
  serializer_class = ProductSerializer
  renderer_classes = [UserRenderer]
  def get(self, request):
    """
    :return: All products stored in database
    check the permission to view the products
    """
    items = Product.objects.all()
    serializer = ProductSerializer(items, many=True)
    return Response({"status": "success", "data": serializer.data}, status = 200)


class GetProductById(GenericAPIView):
  serializer_class = ProductSerializer
  renderer_classes = [UserRenderer]
  def get(self, request, id=None):
    """
    :return: Get all Product by id.
    """
    try:
      if id:
        item = Product.objects.get(id=id)
        serializer = GetProductSerializer(item)
        return Response({"status": "success", "data": serializer.data}, status = 200)
    except:
      return Response({"status": "Not Found"}, status = 400)


class ProductPaginatioNext(GenericAPIView):
  """
  :return: move to next page if the user hit's the api.
  """
  serializer_class = ProductSerializer
  renderer_classes = [UserRenderer]
  def get(self,request,LIMIT=2):
    global OFFSET
    OFFSET,LIMIT = pagination(OFFSET,LIMIT,1)
    res = Product.objects.all()
    if OFFSET>=len(res):
      OFFSET = OFFSET-LIMIT
    res = Product.objects.all()[OFFSET:OFFSET+LIMIT]
    serializer =  ProductSerializer(res, many=True)
    return Response({"status": "success", "data": serializer.data}, status = 200)


class ProductPaginationPrevious(GenericAPIView):
  """
  :return: Move to the previous page if the user hit the api.
  """
  serializer_class = ProductSerializer
  renderer_classes = [UserRenderer]
  def get(self,request,LIMIT=2):
    global OFFSET
    OFFSET,LIMIT = pagination(OFFSET,LIMIT,0)
    res = Product.objects.all()[OFFSET:OFFSET+LIMIT]
    serializer =  ProductSerializer(res, many=True)
    return Response({"status": "success", "data": serializer.data}, status=200)


class GetProductByCategory(GenericAPIView):
  """
  :return: All the product shown by the category.
  """
  serializer_class = ProductSerializer
  renderer_classes = [UserRenderer]
  def get(self,request,id):
    try:
      res = Product.objects.filter(category=id)
      serializer =  ProductSerializer(res, many=True)
      return Response({"status": "success", "data": serializer.data}, status = 200)
    except:
      return Response({"status": "Not Found"}, status = 400)

class GetAllCategory(GenericAPIView):
  """
  :return: Get all the category from the category table.
  """
  serializer_class = CategorySerializer
  renderer_classes = [UserRenderer]
  def get(self, request):
      items = Category.objects.all()
      serializer = CategorySerializer(items, many=True)
      return Response({"status": "success", "data": serializer.data}, status = 200)


class CategoryPaginatioNext(GenericAPIView):
  """
  :return: Move to the next page if the user hit the API.
  """
  serializer_class = CategorySerializer
  renderer_classes = [UserRenderer]
  def get(self,request,LIMIT=2):
    global OFFSET
    OFFSET,LIMIT = pagination(OFFSET,LIMIT,1)
    res = Category.objects.all()
    if OFFSET>=len(res):
      OFFSET = OFFSET-LIMIT
    res = Category.objects.all()[OFFSET:OFFSET+LIMIT]
    serializer =  CategorySerializer(res, many=True)
    return Response({"status": "success", "data": serializer.data}, status = 200)


class CategoryPaginationPrevious(GenericAPIView):
  serializer_class = CategorySerializer
  renderer_classes = [UserRenderer]
  def get(self,request,LIMIT=2):
    """
    :return: Move to the previous page if the user hit the url.
    category pagination 
    """
    global OFFSET
    OFFSET,LIMIT = pagination(OFFSET,LIMIT,0)
    res = Category.objects.all()[OFFSET:OFFSET+LIMIT]
    serializer =  CategorySerializer(res, many=True)
    return Response({"status": "success", "data": serializer.data}, status = 200)