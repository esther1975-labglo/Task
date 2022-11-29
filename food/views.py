from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from food.models import Food, FoodCategory
from restaurant.models import Restaurant
from food.serializers import FoodSerializer, FoodCategorySerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

    # def create(self, request,  *args, **kwargs):


    #     serializer = FoodCategorySerializer(data=request.data)

    #     if not serializer.is_valid():
    #         return Response(serializer.errors)

    #     # if restaurant_pk is None:
    #     #     return Response({'message': 'restaurant required'})

    #     restaurant = Restaurant.objects.get(pk=self.request.data['restaurant'])

    #     serializer.save(restaurant=restaurant)

    #     return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAuthenticated]

    #     return [permission() for permission in permission_classes]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    # def list(self, request, category_pk=None, restaurant_pk=None):
    #     if category_pk is not None and restaurant_pk is not None:
    #         queryset = Food.objects.filter(
    #             category_id=category_pk, restaurant_id=restaurant_pk)
    #     elif restaurant_pk is not None and category_pk is None:
    #         queryset = Food.objects.filter(restaurant_id=restaurant_pk)
    #     else:
    #         queryset = Food.objects.filter(category_id=category_pk)

    #     serializer = FoodSerializer(queryset, many=True)

    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):

        
    #     serializer = FoodSerializer(data=request.data)

    #     if not serializer.is_valid():
    #         return Response(serializer.errors)

    #     foodCategory = FoodCategory.objects.get(
    #         pk=request.data.['category'])
    #     restaurant = Restaurant.objects.get(
    #         pk=request.data.['restaurant'])
    #     serializer.save(category=foodCategory, restaurant=restaurant)

    #     return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAuthenticated]

    #     return [permission() for permission in permission_classes]

