from rest_framework import viewsets
from restaurant.models import Restaurant, Category, Menu
from restaurant.serializers import (
    RestaurantSerializer,
    CategorySerializer,
    MenuSerializer
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    restaurant details
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    restaurant food categories details
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuViewSet(viewsets.ModelViewSet):
    """
    restaurant Menu details
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
