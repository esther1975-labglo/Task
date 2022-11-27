from rest_framework import serializers
from DeliveryPartner.models import Profile, Service, Task


class ProfileSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return profile.objects.create(**validated_data)

    class Meta:
        model = Profile
        fields = ('id', 'name', 'phone_number', 'image',
                  'joining_date')


class ServiceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Service.objects.create(**validated_data)

    class Meta:
        model = Service
        fields = ('total_orders_handled')


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('url', 'restaurant', 'delivery', 'status')