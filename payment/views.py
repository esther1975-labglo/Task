from django.shortcuts import render
from payment.models import Billing
from payment.serializers import BillingSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

class BillingViewSet(viewsets.ModelViewSet):
    """
    payment details of the order
    """
    
    serializer_class = BillingSerializer
    queryset = Billing.objects.all()