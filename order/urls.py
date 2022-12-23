from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order import views
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'order', OrderViewSet)




urlpatterns = [
    path('', include(router.urls)),
    # path('order_payment/', process_payment, name='process_payment'),
    # path('payment-done/', views.payment_done, name='payment_done'),
    # path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    
    ]