from django.db import models
from order.models import Order
from DeliveryPartner.models import Profile
from user.models import User


STATUS_CHOICES = (
        ('S', 'Success'),
        ('P', 'Pending'),
        ('F', 'Failed'),
    )

class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    handled_DeliveryPartner = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null = True)
    delivery_location = models.CharField(max_length = 50)
    status = models.CharField(max_length = 1, null = True, choices = STATUS_CHOICES)
