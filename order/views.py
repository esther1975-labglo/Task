from django.shortcuts import render
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

class OrderViewSet(viewsets.ModelViewSet):

    """
    order details
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

