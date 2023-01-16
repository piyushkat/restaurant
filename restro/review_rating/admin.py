from django.contrib import admin
from review_rating.models import ReviewRating

# Register your models here.

class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('user','products','review','ratings','created_at')
admin.site.register(ReviewRating,ReviewRatingAdmin)