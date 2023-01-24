from django.contrib import admin
from cart.models import Cartitems


# Register your models here.
class CartItemsAdmin(admin.ModelAdmin):
    fields = ['user','product','quantity']
    list_display = ('id','user','quantity')
admin.site.register(Cartitems,CartItemsAdmin)