from rest_framework import serializers
from payment.models import Billing

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = (
            'transaction_id',
            'order',
            'status'
            )