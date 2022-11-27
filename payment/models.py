from django.db import models
from order.models import Order


PAYMENT_STATUS = (
        ('S', 'Success'),
        ('P', 'Pending'),
        ('F', 'Failed'),
    )

PAYMENT_METHOD = (
    ('C', 'CashOnDelivery'),
    ('G', 'GooglePay'),
    ('P', 'PhonePay'),
    ('M', 'Paytm')

)


class Billing(models.Model):
    transaction_id = models.IntegerField(null = False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    payment_method = models.CharField(max_length = 1, null = True, choices = PAYMENT_METHOD)
    status = models.CharField(max_length = 1, null = True, choices = PAYMENT_STATUS)

    
