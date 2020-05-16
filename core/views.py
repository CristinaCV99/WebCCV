
from django.shortcuts import render, HttpResponse

html_base = """
<h>Mi web personal </h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + """
    <h2>Portada</h2>
    <p>This is a portad</p>
    """)

def about(request):
    return HttpResponse(html_base + """
    <h2>Acerca de</h2>
    <p>Me llamo Carmen y soy programadora</p>
    """)
    
# Create your views here.
def portfolio(request):
    return HttpResponse(html_base + """
    <h2>Portafolio</h2>
    <p>Algunos de mis trabajos</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
    <h2>Contact</h2>
    <p>Información de mi contacto</p><a>cris_rockanrolla2299@hotMAIL.com</a></p>
    """)
    