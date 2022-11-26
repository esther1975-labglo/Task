from django.db import models
#from restaurant.models import Restaurant
from user.models import User
from food.models import Food
from django.utils import timezone

STATUS_CHOICES = (
        ('S', 'Success'),
        ('P', 'Pending'),
        ('F', 'Failed'),
    )

class Order(models.Model):
    #restaurant = models.ForeignKey(
   #     Restaurant, related_name="foods", on_delete=models.CASCADE, null=True)
    time_placed = models.TimeField('time placed', null=True)
    is_ready = models.BooleanField(default=False, null=True)
    order_for = models.CharField(max_length=50, null=True)
    pickup_time = models.DateTimeField(default=timezone.now, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    food_items = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, null=True)
    total = models.DecimalField(max_digits=4, null=True, decimal_places=2)
    instructions = models.TextField(max_length=5000, blank=True, null=True)
    status = models.CharField(max_length = 1, null = True, choices = STATUS_CHOICES)

    def __str__(self):
        return self.items
