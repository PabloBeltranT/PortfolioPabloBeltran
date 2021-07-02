from django.urls import path
from .api import portfolio_api, portfolio_api_detail

urlpatterns = [
    path('api/', portfolio_api),
    path('api/<int:id>', portfolio_api_detail),
]