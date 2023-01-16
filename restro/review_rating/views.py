import datetime
from products.models import Product
from rest_framework.generics import GenericAPIView
from review_rating.models import *
from review_rating.serializer import *
from food.renderers import UserRenderer
from rest_framework.response import Response
from datetime import datetime, timedelta

# Create your views here.
class ReviewRatingView(GenericAPIView):
  serializer_class = ReviewRatingSerializer
  renderer_classes = [UserRenderer]
  def post(self,request,id):
    now = datetime.now()
    user = self.request.user
    products = Product.objects.get(id=id)
    review = request.data.get('review')
    ratings = request.data.get('ratings')
    review_rating = ReviewRating.objects.create(user=user,products=products,review=review,ratings=ratings,created_at=now)
    serializer = ReviewRatingSerializer(review_rating)
    return Response({'msg':"success","data":serializer.data}, status = 200)


class GetReviewRating(GenericAPIView):
  serializer_class = ReviewRatingSerializer
  renderer_classes = [UserRenderer]
  def get(self,request,id):
    user = self.request.user
    res = ReviewRating.objects.filter(user=user)
    serializer = ReviewRatingSerializer(res,many=True)
    return Response({'msg':"success","data":serializer.data}, status = 200)