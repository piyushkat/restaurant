from django.urls import path
from meal_req.views import *

urlpatterns = [
     path('medicinerequest', RequestForFood.as_view(), name='delivery'),
     path('orderapprove/<int:id>', FoodOrderApporve.as_view(), name='orderapprove'),
     path('orderdecline/<int:id>', FoodOrderDecline.as_view(), name='orderdecline'),
     path('orderperstore/', FoodRequestPerStore.as_view(), name='orderperstore'),
     path('deliveryboy/<int:id>', DeliveryBoyOrderStatus.as_view(), name='orderperstore'),
]
