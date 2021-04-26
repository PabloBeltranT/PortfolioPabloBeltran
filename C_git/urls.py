from django.urls import path
from .views import git

urlpatterns = [
    path('git/', git),
]
