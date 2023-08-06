from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    matching_series = Trabajador.objects.all()

    return render(request=request,
                  template_name='main/index.html',
                  
                  )

def trabajadores(request, trabajadores: str):
    matching_series = Trabajador.objects.filter(trabajadores__nombre_empleado=trabajadores).all()

    return render(
        request=request,
        template_name='main/home.html',
        context={"objects": matching_series}
    )
    