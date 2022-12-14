from django.db import models
from restaurant.models import Restaurant


class FoodCategory(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(
        Restaurant, related_name="categories", null = True, on_delete=models.CASCADE)


class Food(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'img', null = True)
    category = models.ForeignKey(
        FoodCategory, related_name="foods", on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, related_name="foods", on_delete=models.CASCADE)
    description = models.TextField()
    active = models.BooleanField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_veg = models.BooleanField()
    quantity = models.IntegerField(null = True)
   