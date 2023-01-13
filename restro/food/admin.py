from django.contrib import admin
from food.models import *

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'auth_token', 'is_verified',
                    'is_admin', 'created_at')
admin.site.register(Profile,ProfileAdmin)