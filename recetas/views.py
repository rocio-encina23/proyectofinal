from django.shortcuts import render, redirect
from django.urls import reverse , reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from recetas.forms import CursoFormulario, RecetaFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.db.models import Q

from recetas.models import Todas,Curso

@login_required
def listar_recetas (request):
    contexto= {
    "recetas":Todas.objects.all(),         
    }    
    http_response= render (
        request=request,
        template_name= 'recetas/lista_recetas.html',
        context=contexto,
    )
    return http_response
    
def listar_cursos (request):
    contexto= {
        "cursos":Curso.objects.all(),
            
    }    
    http_response= render (
        request=request,
        template_name= 'recetas/lista_cursos.html',
        context=contexto,
    )
    return http_response
    
#def crear_curso(request):
#    if request.method == "POST":
#       data= request.POST
#       curso= Curso(nombre=data ['nombre'])
#       curso.save()
#       url_exitosa= reverse ('lista_cursos')
#       return redirect (url_exitosa)
#    else: #GET
#        http_response= render(
#            request=request,
#           template_name= 'recetas/formulario_curso_a_mano.html',
#       )
#   return http_response

@login_required
def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  #diccionario
            nombre = data["nombre"]
            curso = Curso(nombre=nombre, creador=request.user)
            curso.save()

            url_exitosa = reverse('lista_cursos')  
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = CursoFormulario()
    return render(
        request=request,
        template_name='recetas/formulario_curso.html',
        context={'formulario': formulario}
    )


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        cursos = Curso.objects.filter(nombre__contains=busqueda)
        

        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='recetas/lista_cursos.html',
            context=contexto,
        )
        return http_response
    
@login_required
def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)

@login_required
def editar_curso(request,id):  
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
       formulario = CursoFormulario(request.POST)

    if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.save()

            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa)
    else:  # GET
        
        inicial = {
            'nombre': curso.nombre,
            }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='recetas/formulario_curso.html',
        context={'formulario': formulario},
            )


@login_required
def crear_receta(request):
    if request.method == "POST":
        formulario = RecetaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  #diccionario
            titulo = data["titulo"]
            todas = Todas(titulo=titulo, creador=request.user)
            todas.save()

            url_exitosa = reverse('lista_recetas')  
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = RecetaFormulario()
    http_response = render(
        request=request,
        template_name='recetas/formulario_receta.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_receta(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        recetas= Todas.objects.filter(titulo__contains=busqueda)
        
        contexto = {
            "recetas": recetas,
        }
        http_response = render(
            request=request,
            template_name='recetas/lista_recetas.html',
            context=contexto,
        )
        return http_response
    
@login_required
def eliminar_receta(request,id):
    receta = Todas.objects.get(id=id)
    if request.method == "POST":
        receta.delete()
        url_exitosa = reverse('lista_recetas')
        return redirect(url_exitosa)

@login_required
def editar_receta(request, id):  
    receta = Todas.objects.get(id=id)
    if request.method == "POST":
       formulario = RecetaFormulario(request.POST)

    if formulario.is_valid():
            data = formulario.cleaned_data
            receta.titulo = data['titulo']
            receta.save()

            url_exitosa = reverse('lista_recetas')
            return redirect(url_exitosa)
    else:  # GET
        
        inicial = {
            'titulo': receta.titulo,
            }
        formulario = RecetaFormulario(initial=inicial)
    return render(
        request=request,
        template_name='recetas/formulario_receta.html',
        context={'formulario': formulario},
            )    


class TodasListView(ListView):
    model = Todas
    template_name= 'recetas/lista_recetas.html'


class TodasCreateView(CreateView):
    model = Todas
    fields= ("titulo", "tipo") 
    success_url= reverse_lazy ('lista_recetas')


class TodasDetailView(DetailView):
    model = Todas
    success_url= reverse_lazy ('lista_recetas')


class TodasUpdateView(UpdateView):
    model = Todas
    fields= ("titulo", "tipo") 
    success_url= reverse_lazy ('lista_recetas')    


class TodasDeleteView(DeleteView):
    model = Todas
    success_url= reverse_lazy ('lista_recetas')

def about_us(request):
    contexto={}
    http_response= render(
        request=request,
        template_name= 'recetas/about_us.html',
        context= contexto
    )
    return http_response


def libro_recomendado(request):
    contexto={
    "libros":Libro.objects.all(),
             }        
       
    http_response= render (
        request= request,
        template_name= 'recetas/libro_recomendado.html',
        context= contexto,
    )
    return http_response




