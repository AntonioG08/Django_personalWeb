from django.shortcuts import render, HttpResponse

# Variable used to practice the HttpResponse tool
html_base = """
<h1> Mi web personal </h1>
<br> </br>

<ul>
    <li><a href="/"> Portada </a></li>
    <li><a href="/about-me/"> Acerca de </a></li>
    <li><a href="/portfolio/"> Mi portafolio </a></li>
    <li><a href="/contact-information/"> Información de contacto </a></li>
</ul>
<br> </br>
"""


# Create your views here (first examples using HttpResponse)
"""
def home(request):
    return HttpResponse(html_base +
                        "<h2> Mi web personal </h2>"
                        "<p> Esta es la página de portada </p>")


def about(request):
    return HttpResponse(html_base +
                        "<h2> Acerca de mi </h2>"
                        "<p> Me llamo Tony y soy ingeniero </p>")


def portafolio(request):
    return HttpResponse(html_base +
                        "<h2> Portafolio personal de trabajo </h2>"
                        "<p> ¡Saludos! este es mi portafolio de trabajo </p>")


def contacto(request):
    return HttpResponse(html_base +
                        "<h2> Información para contactarme </h2>"
                        "<p> Correo: togoruiz08@hotmail.com </p>")
"""


# Create your views here (Views using now the render tool)
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contacto(request):
    return render(request, 'core/contacto.html')




