from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def desktop_gui(request):
    return render(request, 'desktop_gui.html',{})
