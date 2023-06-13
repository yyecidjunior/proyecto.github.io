from django.shortcuts import render, redirect
from .models import Encuesta


# Create your views here.
def home (request):
    return render(request, "index.html")

def encuesta(request):
    return render(request, "encuesta/encuesta.html")

def quienes_somos(request): 
    return render(request, "paginas/Quienes_somos.html")

def informacion(request):
    return render(request, "paginas/informacion.html")


def Gracias(request):
    return render(request, "paginas/Gracias.html")



def registrarRespuestas(request):
    Carrera = request.POST['Carrera']
    Edad = request.POST['Edad']
    Genero = request.POST['Genero']
    R1 = request.POST['R1']
    R2 = request.POST['R2']
    R3 = request.POST['R3']
    R4 = request.POST['R4']
    R5 = request.POST.getlist('R5')
    R6 = request.POST['R6']
    R7 = request.POST['R7']
    R8 = request.POST.getlist('R8')
    R9 = request.POST['R9']
    R10 = request.POST['R10']
    Nombre= request.POST['Nombre']
    Numero_de_Celular= request.POST['Numero_de_Celular']
    
    encuesta = Encuesta.objects.create(Carrera=Carrera, Edad=Edad, Genero=Genero, R1=R1, R2=R2, R3=R3, R4=R4, R5=','.join(R5), R6=R6, R7=R7, R8=','.join(R8), R9=R9, R10=R10, Nombre=Nombre, Numero_de_Celular=Numero_de_Celular)
    
    return redirect('/Gracias/')

