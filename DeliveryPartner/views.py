from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from DeliveryPartner.models import Profile, Service, Task
from DeliveryPartner.serializers import (
    ProfileSerializer, 
    ServiceSerializer,
    TaskSerializer
)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Delivery partner profile details
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    service of the day in delivery
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    task of delivery parner
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer