from django.shortcuts import render, redirect
from .models import Login

# Create your views here.
def login(request):
    if request.method == 'POST':
        try:
            name = request.POST['user']
            password = request.POST['password']
            registred_user = Login.objects.get(name=name, password=password)
            if registred_user:
                return render(request, 'configuration.html', {})
        except:
            return render(request, 'login.html', {'error':'Sesion no encontrada!'})
    else:
        return render(request, 'login.html', {})

def registrar_usuario(request):
    if request.method == 'POST':
        try:
            name = request.POST['user']
            password = request.POST['password']
            email = request.POST['email']
            usuario_registrado = Login.objects.get(name=name)
        except:
            nuevo_usuario = Login(name=name, password=password, email=email)
            nuevo_usuario.save()
            return render(request, 'registrar_usuario.html', {'mensaje':'Registro Exitoso!'})
    else:
        return render(request, 'registrar_usuario.html', {})



def configuration(request):
    return render(request, 'configuration.html',{})

def viewer(request):
    return render(request, 'viewer.html',{})