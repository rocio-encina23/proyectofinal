from django.urls import path 

from recetas.views import (
    about_us,listar_recetas, listar_cursos, crear_curso, buscar_cursos,eliminar_curso,editar_curso,
    crear_receta, buscar_receta, eliminar_receta,editar_receta,
    TodasListView, TodasCreateView, TodasDeleteView,TodasDetailView,TodasUpdateView )

from .views import *
from .models import *


# Son las URLS de la app 
urlpatterns = [
    #URL Cursos
    path('about-us', about_us, name="about-us" ),
    path('recetas/', listar_recetas, name="lista_recetas"),
    path('cursos/', listar_cursos, name="lista_cursos"),
    path('crear-curso/',crear_curso, name="crear_curso"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path("eliminar-curso/<int:id>/", eliminar_curso, name="eliminar_curso"),
    path("editar-curso/<int:id>/", editar_curso, name="editar_curso"),
    #URL de recetas
    path('crear-receta/', crear_receta, name="crear_receta"),
    path('buscar-receta/', buscar_receta, name='buscar_receta'),
    path('eliminar-receta/<int:id>/', eliminar_receta, name='eliminar_receta'),
    path('editar-receta/<int:id>/', editar_receta, name='editar_receta'),
    path('libros-recomendados/', libro_recomendado, name="libro_recomendado"),

    path('recetas/', TodasListView.as_view(), name='lista_recetas'),
    path("receta/<int:pk>/", TodasDetailView.as_view(), name="ver_receta"),
    path("crear-receta/", TodasCreateView.as_view(), name="crear_receta"),
    path("editar-receta/<int:pk>/", TodasUpdateView.as_view(), name="editar_receta"),
    path("eliminar-receta/<int:pk>/", TodasDeleteView.as_view(), name="eliminar_receta"),
]
