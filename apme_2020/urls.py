from django.urls import path
from .views import login, configuration, viewer

urlpatterns = [
    path('login/', login),
    path('configuration/', configuration),
    path('viewer/', viewer),
]
