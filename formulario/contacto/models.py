from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.TextField()
    numero = models.CharField(max_length=200)