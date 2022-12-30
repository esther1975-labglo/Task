from django.conf.urls import url
from django.urls import path, include
from .views import UploadFileView
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'csv', views.CsvViewSet)
urlpatterns = [
   
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('', include(router.urls)),
]