from django.db import models
from restaurant.models import Restaurant
from user.models import User
from django.core.validators import RegexValidator

STATUS_CHOICES = (
        ('S', 'Success'),
        ('P', 'Pending'),
        ('F', 'Failed'),
    )

class Profile(models.Model):
    name = models.CharField(max_length = 50)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed."
        )
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)  
    image = models.ImageField(null = True, upload_to = 'img')
    joining_date = models.DateField(null = True)
             
class Service(models.Model):
    total_orders_handled = models.IntegerField(null = True)

class Task(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)
    delivery_location = models.CharField(max_length = 50)
    status = models.CharField(max_length = 1, null = True, choices = STATUS_CHOICES)





