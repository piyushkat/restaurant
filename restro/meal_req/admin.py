from django.contrib import admin
from meal_req.models import RequestMedicine,StoreInfo,OrderStatus,DeliveryBoy

# Register your models here.

class RequestMedicineAdmin(admin.ModelAdmin):
    fields = ['cart','phone_no', 'address','latitude', 'longitude', 'user']
    list_display = ('id','phone_no', 'address','latitude', 'longitude', 'user', 'date')
admin.site.register(RequestMedicine, RequestMedicineAdmin)


class OrderStatusAdmin(admin.ModelAdmin):
    fields = ['cart','store_info','status']
    list_display = ('store_info', 'date', 'status')
admin.site.register(OrderStatus, OrderStatusAdmin)


class StoreInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude','longitude', 'owner', 'date')
admin.site.register(StoreInfo, StoreInfoAdmin)


class DeliveryBoyAdmin(admin.ModelAdmin):
    fields= ['user','order']
    list_display = ('user','date')
admin.site.register(DeliveryBoy,DeliveryBoyAdmin)
