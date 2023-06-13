from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('encuesta/',views.encuesta, name='encuesta'),
    path('quienes_somos/',views.quienes_somos, name='quienes_somos'),
    path('informacion/', views.informacion, name='informacion'),
    path('Gracias/', views.Gracias, name='Gracias'),
    path('registrarRespuestas/', views.registrarRespuestas, name='registrarRespuestas' )
]