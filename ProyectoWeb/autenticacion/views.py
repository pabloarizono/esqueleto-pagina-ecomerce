from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .forms import RegistroForm
# Create your views here.


from django.contrib import messages
from .forms import RegistroForm

from django.conf import settings
from django.db import models
from django.contrib import messages




#form=AuthenticationForm(request, data=request.POST)
#if form.is_valid():
def cerrar_sesion(request):
    logout(request)

    return redirect('home')

def logear(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        usuario=authenticate(username=username, password=password)
        
        if usuario is not None:
            login(request, usuario)
            return redirect("home")
        else:
             messages.info(request, "usuario o contraseña no válido")

    contexto={}
    return render(request,"login/login.html",contexto)





def registro(request):
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username},por favor inicia sesion!')
            return redirect('home')
    
    contexto ={'form':form}
    return render(request, 'registro/registro.html', contexto)

    

        
