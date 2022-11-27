from django.urls import path, include
from rest_framework.routers import DefaultRouter
from DeliveryPartner import views
from .views import (

    ProfileViewSet,
    ServiceViewSet,
    TaskViewSet
   
)

router = DefaultRouter()
router.register(r'profile_of_deliveryPartner', ProfileViewSet)
router.register(r'today_service_of_delivery_partner', ServiceViewSet)
router.register(r'delivery_man_task', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]



