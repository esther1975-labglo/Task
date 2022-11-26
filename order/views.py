from django.shortcuts import render
from order.models import Order

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

