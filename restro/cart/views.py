import datetime
from cart.models import *
from food.renderers import UserRenderer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from cart.serializer import AddCartSerializer,ViewCartSerializer,DeleteCartSerializer
# Create your views here.


class AddProductCart(GenericAPIView):
  serializer_class = AddCartSerializer
  renderer_classes = [UserRenderer]
  def post(self,request,id): 
    try:
      if not self.request.user.is_authenticated:
        return Response({'msg':'user not found'})
      user = User.objects.get(id=id)
      product = Product.objects.get(id=request.data['product_id'])
      quantity = int(request.data['quantity'])   
      try:
        cart=Cartitems.objects.get(user=user,product=product)
        cart.quantity += quantity
      except:
        cart=Cartitems.objects.create(user=user,product=product,quantity=quantity,created_at=datetime.datetime.now)
      cart.save()
      serializer = AddCartSerializer(cart)
      return Response({"status":"success", "data": serializer.data}, status = 200)
    except:
      return Response({"status":"Not Found"}, status = 400)


class ViewCartProduct(GenericAPIView):
  serializer_class = ViewCartSerializer
  renderer_classes = [UserRenderer]
  def get(self, request,id):
    user = User.objects.get(id=id)
    cart = Cartitems.objects.filter(user=user)
    serializer = ViewCartSerializer(cart,many=True)
    return Response({"status": "success", "data": serializer.data}, status = 200)


class DeleteCartItemById(GenericAPIView):
  serializer_class = DeleteCartSerializer
  renderer_classes = [UserRenderer]
  def post(self,request,id):
    try:
      user = User.objects.filter(id=id)
      cart = Cartitems.objects.get(id=id).delete()
      serializer = ViewCartSerializer(cart)
      return Response({"status": "success", "data": serializer.data}, status = 200)
    except:
      return Response({"status": "Not available"}, status = 400)


class DeleteCartItem(GenericAPIView):
  serializer_class = DeleteCartSerializer
  renderer_classes = [UserRenderer]
  def post(self,request,id):
    user = User.objects.filter(id=id)
    cart = Cartitems.objects.all().delete()
    serializer = DeleteCartSerializer(cart)
    return Response({"status": "success", "data": serializer.data}, status = 200)