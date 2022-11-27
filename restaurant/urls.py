from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from .views import (
    RestaurantViewSet,
    CategoryViewSet,
    MenuViewSet
)

router = DefaultRouter()
router.register(r'restaurant', RestaurantViewSet)
router.register(r'restaurant_category', CategoryViewSet)
router.register(r'restaurant_menu', MenuViewSet)




urlpatterns = [
    path('', include(router.urls)),
    
    ]