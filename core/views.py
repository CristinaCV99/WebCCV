
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
    return render(request, "core/home.html")
   

def about(request):
    return render(request, "core/about.html")

    
# Create your views here.
def portfolio(request):
    return render(request, "core/portfolio.html")


def contact(request):
    return render(request, "core/contact.html")

    