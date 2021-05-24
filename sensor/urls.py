from django.urls import path
from .views import sensor

urlpatterns = [
    path('sensor/', sensor),
]
