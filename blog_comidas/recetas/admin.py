from django.contrib import admin

from recetas.models import Todas, Curso, Saladas, Dulces, Veganas

admin.site.register(Todas)
admin.site.register(Curso)
admin.site.register(Saladas)
admin.site.register(Dulces)
admin.site.register(Veganas)

