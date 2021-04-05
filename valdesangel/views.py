from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context

# Create your views here.
def prueba1(request):
	externo = open("C:/Users/Angel/Desktop/djangoPasos/examenu3/templates/prueba.html")
	plantilla = Template(externo.read())
	externo.close() #abre, lee y ahora cierralo 
	ctx = Context()
	contenido = plantilla.render(ctx)
	return HttpResponse(contenido)
	##paso por paso para respuesta con el navegador 

def prueba2(request):
	return render(request,"prueba.html")