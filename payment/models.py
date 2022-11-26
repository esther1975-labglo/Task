from django.db import models
from order.models import Order


PAYMENT_CHOICES = (
        ('S', 'Success'),
        ('P', 'Pending'),
        ('F', 'Failed'),
    )

class Billing(models.Model):
    transaction_id = models.IntegerField(null = False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length = 1, null = True, choices = PAYMENT_CHOICES)

    
