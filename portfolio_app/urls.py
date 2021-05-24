from django.urls import path
from .views import index, desktop_gui

urlpatterns = [
    path('', index),
    path('desktop_gui/', desktop_gui),
]
