from django.urls import path, include
from rest_framework.routers import DefaultRouter
from food import views
from .views import (

    FoodCategoryViewSet,
    FoodViewSet
   
)

router = DefaultRouter()
router.register(r'food_category', FoodCategoryViewSet)
router.register(r'food', FoodViewSet)



urlpatterns = [
    path('', include(router.urls)),
    
]