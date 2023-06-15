from django.db import models

# Create your models here.
class Cargo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
	    return self.nombre

class Profesional(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    especialista = models.BooleanField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="profesional", null=True)

    def __str__(self):
	    return self.nombre
    
tipos_contacto = [
    [0, "Sugerencia"],
    [1, "Reclamo"]
]    

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    tipo_contacto = models.IntegerField(choices=tipos_contacto)
    mensaje = models.TextField() #corresponde a un texto mas largo

    def __str__(self):
	    return self.nombre + " "+self.email

