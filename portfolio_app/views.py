from django.shortcuts import render
from datetime import date
from .models import Visits

# Create your views here.
def index(request):
    last_update = date.today()
    visit = request.META['DESKTOP_SESSION']
    new_visit = Visits(from_to=visit)
    new_visit.save()
    visits = Visits.objects.all()
    cant = 0
    for visitant in visits:
        cant = cant + 1
    return render(request, 'index.html', {'last_update':last_update, 'visits':cant})

def desktop_gui(request):
    return render(request, 'desktop_gui.html',{})
