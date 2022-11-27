from rest_framework import serializers
from Delivery.models import Delivery


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ('url', 'user', 'handled_DeliveryPartner', 
                 'order', 'delivery_location', 'status')
