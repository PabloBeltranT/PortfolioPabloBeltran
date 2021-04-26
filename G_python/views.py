from django.shortcuts import render

def python(request):
    return render(request, 'python.html', {'title':'Python'})