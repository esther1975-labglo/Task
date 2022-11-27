from rest_framework import serializers
from order.models import Order

'''class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
             'time_placed', 'is_ready', 
            'order_for', 'pickup_time', 'food_items',
            'user', 'quantity', 'total', 'instructions'
            )'''

class OrderSerializer(serializers.ModelSerializer): 
    total_sum = serializers.SerializerMethodField("get_total_sum", read_only=True)
    class Meta: 
        model = Order
        fields = (
             'time_placed', 'is_ready', 
            'order_for', 'pickup_time', 'food_items',
            'user', 'quantity', 'total', 'instructions'
            )
    
    def get_total_summa(self, obj):
        return obj.order.annotate(per_item_price=F('Food_price')*F('quantity')).annotate(total_summa=Sum('per_item_price')).values('total_sum')   