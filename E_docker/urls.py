from django.urls import path
from .views import docker

urlpatterns = [
    path('docker/', docker),
]
