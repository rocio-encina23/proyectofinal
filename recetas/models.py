from django.db import models
from django.contrib.auth.models import User

class Todas(models.Model):
     tipo= models.CharField(max_length=100)
     titulo= models.CharField(max_length=100)
     creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
     def __str__(self):
        return f"{self.tipo}, {self.titulo}"


class Curso(models.Model):
   nombre = models.CharField(max_length=64)
   creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
   def __str__(self):
       return f"{self.nombre}"


class Libro(models.Model):
    titulo=models.CharField(max_length=64)
    autor=models.CharField(max_length=64)
    imagenLibro = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    def __str__(self):
        return self.titulo
   
class Saladas(models.Model):
     titulo= models.CharField(max_length=100)
     tiempo_de_coccion= models.TextField(blank=True, null=True)
     ingredientes= models.TextField(blank=False, null=False)
     pasos= models.TextField(blank=False, null=False)
     tips= models.TextField(blank=True, null=True)
   
     
     def __str__(self):
        return f"{self.titulo}"
  
class Dulces(models.Model):
     titulo= models.CharField(max_length=256)
     calorias_por_porcion= models.TextField(blank=False, null=False)
     tiempo_de_coccion= models.TextField(blank=False, null=False)
     ingredientes= models.TextField(blank=False, null=False)
     pasos= models.TextField(blank=False, null=False)
     
     
     def __str__(self):
        return f"{self.titulo}"
     
class Veganas(models.Model):
     titulo= models.CharField(max_length=256)
     tiempo_de_coccion= models.TextField(blank=False, null=True)
     ingredientes= models.CharField(max_length=256)
     ingredientes_alternativos= models.TextField(blank=True, null=True)
     pasos= models.TextField(blank=False, null=False)
     
     
     def __str__(self):
        return f"{self.titulo}"
     

