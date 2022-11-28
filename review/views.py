from django.shortcuts import render
from rest_framework import viewsets
from review.models import FoodReview, RestaurantReview
from review.serializers import FoodReviewSerializer, RestaurantReviewSerializer
    



class FoodReviewViewSet(viewsets.ModelViewSet):
    """
    food review details
    """
    queryset = FoodReview.objects.all()
    serializer_class = FoodReviewSerializer


class RestaurantReviewViewSet(viewsets.ModelViewSet):
    """
    restaurant review details
    """
    queryset = RestaurantReview.objects.all()
    serializer_class = RestaurantReviewSerializer