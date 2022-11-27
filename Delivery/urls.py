from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Delivery import views
from .views import DeliveryViewSet
   


router = DefaultRouter()
router.register(r'delivery_details', DeliveryViewSet)



urlpatterns = [
    path('', include(router.urls)),
    
]