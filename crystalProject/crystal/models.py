from django.db import models

# Create your models here.

class incidente(models.Model):
    document = models.CharField(max_length = 50, verbose_name= "Documento")
    date = models.DateField(verbose_name= "Fecha")
    user = models.CharField(max_length = 50, verbose_name= "Usuario")
    hour = models.CharField(max_length = 5, verbose_name= "Hora")
    zone = models.CharField(max_length = 20, verbose_name= "Barrio")
    address = models.CharField(max_length = 50, verbose_name= "Direccion")
    brand = models.CharField(max_length = 50, blank = True, null = True, verbose_name= "Marca")
    model = models.CharField(max_length = 50, blank = True, null = True, verbose_name= "Modelo")
    registrationNumber = models.CharField(max_length = 50, blank = True, null = True, verbose_name= "Matricula")
    created_at = models.DateTimeField(auto_now_add = True)