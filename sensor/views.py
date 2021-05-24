from django.shortcuts import render
from random import randint
from .static.sensor.solicitar_info import solicitar

# Create your views here.
def sensor(request):
    return render(request, 'sensor.html', {'corriente': '0.0000',
                                          'pot_directa': '1638 W',
                                          'pot_red': '53 W',
                                          'fuente': 'Fuente',
                                          }
                )