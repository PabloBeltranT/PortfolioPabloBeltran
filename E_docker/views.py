from django.shortcuts import render

def docker(request):
    return render(request, 'docker.html', {'title':'Docker'})