from rest_framework import serializers
from restaurant.models import Restaurant, Category, Menu
from food.serializers import FoodCategorySerializer



class RestaurantSerializer(serializers.ModelSerializer):

    categories = FoodCategorySerializer(many=True, read_only=True)


    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    class Meta:
        model = Restaurant
        fields = (
            'id', 'user', 'restaurant_name', 
            'slug', 'address', 'city', 
            'restaurant_phone_number', 'restaurant_email',
            'owner_email', 'opening_status', 'features',
            'timings', 'opening_from', 'opening_to', 'other_details',
            'available', 'created', 'updated', 'categories'
            )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'category',
            'restaurant',
            'name',
            'slug',
            'image',
            'description',
            'price',
            'stock',
            'available',
            'created',
            'updated'
        )

class LocationSerializer(serializers.Serializer):
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)


# class  GeoLocationSerializer(serializers.ModelSerializer):
#     location = LocationSerializer(many=True)

#     class Meta:
#         model = GeoLocation
#         fields = ['date', 'location']       