from django.urls import path
from meal_req.views import *

urlpatterns = [
     path('medicinerequest', DeliveryProcess.as_view(), name='delivery'),
     path('orderapprove/<int:id>', MedicineOrderApporve.as_view(), name='orderapprove'),
     path('orderdecline/<int:id>', MedicineOrderDecline.as_view(), name='orderdecline'),
     path('partially/<int:id>', PartiallyFoundMedicine.as_view(), name='partiallyfound'),
     path('orderperstore/', MedicineRequestPerStore.as_view(), name='orderperstore'),
]
