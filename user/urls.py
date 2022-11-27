from django.urls import path

from .views import (
    register_restaurant, 
    register_customer, 
    token, 
    refresh_token, 
    revoke_token,
    LoginView
)

urlpatterns = [
    path('register/customer', register_customer),
    path('register/restaurant', register_restaurant),
    path('login', LoginView.as_view()),
    path('token/', token),
    path('token/refresh/', refresh_token),
    path('token/revoke/', revoke_token),
]