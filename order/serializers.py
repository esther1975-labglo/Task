from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer): 
   
    class Meta: 
        model = Order
        fields = (
             'time_placed', 'is_ready', 
            'order_for', 'pickup_time', 'food_items',
            'user', 'quantity', 'total', 'instructions'
            )
    
       