from django.shortcuts import render, HttpResponse
from .models import comentario


def index(request):
    context={"template_padre": "index"}
    return render(request, "index.html",context)

def preguntas(request):
    context={"template_padre": "preguntas"}
    return render(request, "preguntas.html",context)

def informacion(request):
    context={"template_padre": "informacion"}
    return render(request, "informacion.html",context)

def estadistica(request):
    context={"template_padre": "estadistica"}
    return render(request, "estadistica.html",context)

def comentarios(request):

    if request.method== "POST":
        titulo= request.POST.get('titulo','')
        comentario= request.POST.get('comentarios','')
        autor= request.POST.get('autor','')
        estrellas= request.POST.get('estrellas','')   
        nuevo_comentario= comentario()
        nuevo_comentario.titulo=titulo
        nuevo_comentario.comentario=comentario
        nuevo_comentario.autor=autor
        nuevo_comentario.estrellas=estrellas
        nuevo_comentario.save()
             
            

    context={"template_padre": "comentarios"}
    return render(request, "comentarios.html",context)
            
