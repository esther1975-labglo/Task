from django.urls import path, include
from rest_framework.routers import DefaultRouter
from review import views
from .views import FoodReviewViewSet, RestaurantReviewViewSet

router = DefaultRouter()
router.register(r'food_reviews', FoodReviewViewSet)
router.register(r'restaurant_reviews', RestaurantReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    ]