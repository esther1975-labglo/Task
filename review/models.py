from django.db import models
from user.models import User
from food.models import Food
from restaurant.models import Restaurant



class FoodReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.TextField(null = True)


class RestaurantReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.TextField(null = True)
