from django.shortcuts import render
from .models import project
from pylint import *


# Create your views here.
def portafolio(request):
    proyectos = project.objects.all()
    return render(request, 'portfolio/portafolio.html', {'proyectos': proyectos})
