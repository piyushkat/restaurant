from django.urls import path
from review_rating.views import *

urlpatterns = [
    
    path('reviewrating/<int:id>',ReviewRatingView.as_view(), name='reviewratingview'),
    path('getreviewrating/<int:id>',GetReviewRating.as_view(), name='getreviewratingview'),
    
]