from django.urls import path
from .views import personal_info

urlpatterns = [
    path('personal_info/', personal_info),
]
