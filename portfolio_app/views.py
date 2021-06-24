
from django import views
from django.shortcuts import render
from datetime import date
from .models import Visits, Projects

from django.views import View
from django.http import JsonResponse

# Create your views here.
def index(request):
    last_update = date.today()
    new_visit = Visits(from_to=request)
    new_visit.save()
    visits = Visits.objects.all()
    cant = 0
    for visitant in visits:
        cant = cant + 1
    projects = Projects.objects.all()
    return render(request, 'index.html', {'last_update':last_update, 'visits':cant, 'Projects':projects})

def desktop_gui(request):
    return render(request, 'desktop_gui.html',{})

def notes(request):
    return render(request, 'notes_django_1.html', {})



class PortfolioApi(View):
    
    def get(self, request):
        projects = Projects.objects.all()
        return JsonResponse(list(projects.values()), safe=False)
