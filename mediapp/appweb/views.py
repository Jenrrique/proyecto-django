from django.shortcuts import render
from .models import Profesional
from .forms import ContactoForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def contacto(request):

    data = {
        'form': ContactoForm,
        'mensaje':""
    }

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto Guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Error al ingresar formulario"    

    return render(request, "contacto.html")

def profesionales(request):
    #variable
    profesionales = Profesional.objects.all()

    profesionales = Profesional.objects.raw("select * from appweb_profesional where especialista = true")
    #objeto para enviar al template
    data = {
        'profesionales': profesionales
    }
    return render(request, "profesionales.html")
    
def agregar_profesional(request):
    return render(request, "mantenedor/profesional/agregar.html")

def login_usuario(request):
    print("Bienvenido: " + request.user.username)
    print("este es el login")
    return redirect(to="home")