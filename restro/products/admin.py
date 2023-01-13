from django.contrib import admin
from products.models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'quantity',
                    'price', 'price_before_disc', 'in_stock', 'status', 'category')
    readonly_fields = ('price', 'price_before_disc', 'in_stock', 'status')


admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'image')
admin.site.register(Category,CategoryAdmin)