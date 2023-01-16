from django.contrib import admin
from cart.models import Cartitems


# Register your models here.
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('id','user','product','quantity')
admin.site.register(Cartitems,CartItemsAdmin)