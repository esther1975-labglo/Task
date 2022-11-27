
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payment import views
from .views import BillingViewSet

router = DefaultRouter()
router.register(r'billing_payment', BillingViewSet)




urlpatterns = [
    path('', include(router.urls)),
    
    ]
