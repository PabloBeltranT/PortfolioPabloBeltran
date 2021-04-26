from django.shortcuts import render

def principal(request):
    return render(request, 'portfolio.html', {})