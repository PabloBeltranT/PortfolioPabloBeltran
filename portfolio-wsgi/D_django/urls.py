from django.urls import path
from .views import django, login, configuration, real_time_viewer

urlpatterns = [
    path('django/', django),
    path('login/', login),
    path('configuration/', configuration),
    path('real_time_viewer/', real_time_viewer),
]
