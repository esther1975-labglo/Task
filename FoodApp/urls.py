"""FoodApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from food import urls as food_urls
from restaurant import urls as restaurant_urls
from user import urls as user_urls
from order import urls as order_urls
from payment import urls as payment_urls
from DeliveryPartner import urls as DeliveryPartner_urls
from Delivery import urls as Delivery_urls
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('food/', include(food_urls)),
    path('restaurant/', include(restaurant_urls)),
    path('', include(user_urls)),
    path('order/', include(order_urls)),
    path('payment/', include(payment_urls)),
    path('deliveryPartner/', include(DeliveryPartner_urls)),
    path('delivery/', include(Delivery_urls)),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
