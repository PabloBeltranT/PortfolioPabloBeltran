from django.urls import path, include
from .views import index, desktop_gui, notes

urlpatterns = [
    path('', index),
    path('desktop_gui/', desktop_gui),
    path('notes/', notes),
]


