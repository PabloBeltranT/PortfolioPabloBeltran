from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html',{})

def configuration(request):
    return render(request, 'configuration.html',{})

def viewer(request):
    return render(request, 'viewer.html',{})