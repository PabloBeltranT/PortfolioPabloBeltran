from django.urls import path
from .views import login, configuration, viewer, registrar_usuario

urlpatterns = [
    path('login/', login, name='login'),
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    
    path('configuration/', configuration),
    path('viewer/', viewer, name='viewer'),
]
