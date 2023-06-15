from django.contrib import admin
from .models import *

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
        list_display = ['nombre', 'telefono', 'mensaje', 'email']
        list_editable = ['email']
        search_fields = ['nombre']
        list_filter = ['tipo_contacto']   

class ProfresionalAdmin(admin.ModelAdmin):
        list_display= ['nombre', 'apellido', 'fecha_nacimiento', 'especialista']
        list_editable= ['apellido']
        search_fields= ['rut']
        list_filter= ['especialista']

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Cargo)
admin.site.register(Profesional, ProfresionalAdmin)

