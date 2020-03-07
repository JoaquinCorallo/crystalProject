from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from .forms import incidenteForm
from .models import incidente


def TodosLosIncidentesReportados(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, 'crystal/TodosLosIncidentesReportados.html')
    # En otro caso redireccionamos al login
    return redirect('/index/')


def IncidentesReportadosPorElUsuario(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, 'crystal/IncidentesReportadosPorElUsuario.html')
    # En otro caso redireccionamos al login
    return redirect('/index/')


# login, register y logout


def index(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'crystal/index.html', {'form': form})


def RegistroDeUsuario(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "crystal/RegistroDeUsuario.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


def ReportarIncidente(request):
    if request.user.is_authenticated:
        # Creamos un formulario vacío
        form = incidenteForm()

        # Comprobamos si se ha enviado el formulario
        if request.method == "POST":
            # Añadimos los datos recibidos al formulario
            form = incidenteForm(request.POST)
            # Si el formulario es válido...
            if form.is_valid():
                # Guardamos el formulario pero sin confirmarlo,
                # así conseguiremos una instancia para manejarla
                instancia = form.save(commit=False)
                # Podemos guardarla cuando queramos
                instancia.save()
                # Después de guardar redireccionamos a la lista
                return redirect('/IncidentesReportadosPorElUsuario/')

        # Si llegamos al final renderizamos el formulario
        return render(request, "crystal/ReportarIncidente.html", {'form': form})
        # En otro caso redireccionamos al login
    return redirect('/index/')

def IncidentesEnElMapa(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, 'crystal/IncidentesEnElMapa.html')
    # En otro caso redireccionamos al login
    return redirect('/index/')

def Ajustes(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, 'crystal/Ajustes.html')
    # En otro caso redireccionamos al login
    return redirect('/index/')
