from django.urls import path, include
from .views import home, profesionales, contacto, agregar_profesional, login_usuario

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name ="home"),
    path('profesionales/', profesionales, name="profesionales"),
    path('contacto/', contacto, name="contacto"),
    path('mantenedor/profesional/agregar', agregar_profesional, name="agregar_profesional"),

    path('login_usuario/', login_usuario, name="login_usuario")
]