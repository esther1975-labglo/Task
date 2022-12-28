from django.conf.urls import url
from django.urls import path, include
from .views import UploadFileView

urlpatterns = [
   
    path('upload/', UploadFileView.as_view(), name='upload-file')
]