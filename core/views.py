
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h>Mi web personal </h1><h2>Portada</h2>")
    
