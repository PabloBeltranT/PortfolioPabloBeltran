from django.urls import path
from .views import index, menu

urlpatterns = [
    path('', index),
    path('menu/', menu),
]
