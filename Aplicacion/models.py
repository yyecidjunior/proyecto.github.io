from django.db import models
from .choices import res, sexos,OPCIONES_EMPRESAS,Pedidos

# Create your models here.
class Encuesta(models.Model):
    Carrera=models.CharField(max_length=100)
    Edad=models.CharField(max_length=200)
    Genero=models.CharField(max_length=1, null=False, choices=sexos)
    R1=models.CharField(max_length=1, null=False, choices=res)
    R2=models.CharField(max_length=1, null=False, choices=res)
    R3=models.CharField(max_length=1, null=False, choices=res)
    R4=models.CharField(max_length=1, null=False, choices=res)
    R5 =models.CharField(max_length=100, choices=OPCIONES_EMPRESAS)
    R6=models.CharField(max_length=1, null=False, choices=res)
    R7=models.CharField(max_length=1, null=False, choices=res)
    R8=models.CharField(max_length=100, null=False, choices=Pedidos)
    R9=models.CharField(max_length=1000, null=True)
    R10=models.CharField(max_length=1000)
    Nombre=models.CharField(max_length=200, null=True)
    Numero_de_Celular=models.CharField(max_length=200, null=True)