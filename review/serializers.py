from rest_framework import serializers
from review.models import FoodReview, RestaurantReview

class FoodReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodReview
        fields = (
            'user', 'food', 'comments'
            )

class RestaurantReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantReview
        fields = (
            'user', 'restaurant', 'comments'
            )

