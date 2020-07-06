from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('preguntas',views.preguntas,name="preguntas"),
    path('informacion',views.informacion,name="informacion"),
    path('estadistica',views.estadistica,name="estadistica"),
    path('comentarios',views.comentarios,name="comentarios"),
]

