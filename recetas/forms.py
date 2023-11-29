from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)

class RecetaFormulario(forms.Form):
    titulo = forms.CharField(required=True, max_length=64)  
    ingredientes= forms.CharField(required=True, max_length=64) 
    pasos= forms.CharField(required=True, max_length=64) 