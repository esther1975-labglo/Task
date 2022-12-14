from django.db import models

from user.models import User
from food.models import Food
from DeliveryPartner.models import Profile
from django.utils import timezone

STATUS_CHOICES = (
        ('S', 'Success'),
        ('P', 'Pending'),
        ('F', 'Failed'),
    )

class Order(models.Model):
   
    time_placed = models.TimeField('time placed', null=True)
    is_ready = models.BooleanField(default=False, null=True)
    order_for = models.CharField(max_length=50, null=True)
    pickup_time = models.DateTimeField(default=timezone.now, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    food_items = models.ManyToManyField(Food)
    quantity = models.IntegerField(null = True)
    total = models.DecimalField(max_digits = 5, decimal_places = 2, null=True)
    instructions = models.TextField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length = 1, null = True, choices = STATUS_CHOICES)

    @property
    def price(self):
        total= self.quantity * self.food_items.price
        return total
    
    