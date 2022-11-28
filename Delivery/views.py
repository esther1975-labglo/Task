from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from Delivery.models import Delivery
from Delivery.serializers import (
    DeliverySerializer
)


class DeliveryViewSet(viewsets.ModelViewSet):
    """
    Delvery details 
    """
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer