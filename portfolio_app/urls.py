from django.urls import path
from .views import index, desktop_gui, notes, PortfolioApi

urlpatterns = [
    path('', index),
    path('desktop_gui/', desktop_gui),
    path('notes/', notes),
    path('api/', PortfolioApi.as_view()),
]
