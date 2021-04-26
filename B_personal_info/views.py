from django.shortcuts import render

def personal_info(request):
    return render(request, 'personal_info.html', {})