from django.urls import path
from meal_req.views import *

urlpatterns = [
     path('userdetail/<int:id>', UserAddressDetail.as_view(), name='userdetail'),
     path('viewuserdetail/<int:id>', ViewUserAddressDetail.as_view(), name='viewuserdetail'),
     path('userdetailupdate/<int:id>', UserAddressDetailUpdate.as_view(), name='userdetailupdate'),
     path('deleteuserdetail/<int:id>', DeleteUserAddressDetail.as_view(), name='deleteuserdetail'),
     # path('orderapprove/<int:id>', FoodOrderApporve.as_view(), name='orderapprove'),
     # path('orderdecline/<int:id>', FoodOrderDecline.as_view(), name='orderdecline'),
     # path('orderperstore', FoodRequestPerStoreByUser.as_view(), name='orderperstore'),
     path('orderassigntodeliveryboy/<int:id>', OrderAssignToDeliveryBoy.as_view(), name='orderperstore'),
     path('orderassign/<int:id>', OrderAssignGet.as_view(), name='orderperstore'),
     path('deliveryboyorderstatus/<int:id>', DeliveryBoyOrderStatus.as_view(), name='orderperstore'), # Order status id in the url
     path('deliveryboyorderget', DeliveryBoyOrderGet.as_view(), name='orderperstore'), # Order get by user
     path('radius/<int:id>', RadiusFind.as_view(), name='orderperstore'), # Find the radius of user to 10km
]