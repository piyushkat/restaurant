from rest_framework import serializers
from review_rating.models import ReviewRating

class ReviewRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewRating
        fields = ('id','user','products','review','ratings','created_at')