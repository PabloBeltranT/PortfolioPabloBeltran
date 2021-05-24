from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    last_update = date.today()
    return render(request, 'index.html', {'last_update':last_update})

def desktop_gui(request):
    return render(request, 'desktop_gui.html',{})
