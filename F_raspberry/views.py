from django.shortcuts import render

def raspberry(request):
    return render(request, 'raspberry.html', {'title':'Raspberry Pi'})