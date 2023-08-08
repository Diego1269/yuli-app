from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from .decorators import user_is_superuser
from .forms import *

# Create your views here.
def homepage(request):
    matching_series = Trabajador.objects.all()

    return render(request=request,
                  template_name='main/index.html',
                  )

@user_is_superuser
def panel(request):
    matching_series = Trabajador.objects.all()

    return render(request=request,
                  template_name='main/home.html',
                  )

@user_is_superuser
def trabajadores(request):
    matching_series = Trabajador.objects.all()

    return render(
        request=request,
        template_name='main/lista.html',
        context={"objects": matching_series,
                 "type": "trabajadores"}
    )

@user_is_superuser
def contratos(request):
    matching_series = Contrato.objects.all()

    return render(
        request=request,
        template_name='main/lista.html',
        context={"objects": matching_series,
                 "type": "contratos"}
    )

@user_is_superuser
def ventas(request):
    matching_series = Venta.objects.all()

    return render(
        request=request,
        template_name='main/lista.html',
        context={"objects": matching_series,
                 "type": "ventas"}
    )

@user_is_superuser
def ubicaciones(request):
    matching_series = Ubicacion.objects.all()

    return render(
        request=request,
        template_name='main/lista.html',
        context={"objects": matching_series,
                 "type": "ubicaciones"}
    )

@user_is_superuser
def salones(request):
    matching_series = Salon.objects.all()

    return render(
        request=request,
        template_name='main/lista.html',
        context={"objects": matching_series,
                 "type": "salones"}
    )

@user_is_superuser
def templos(request):
    matching_series = Templo.objects.all()

    return render(
        request=request,
        template_name='main/lista.html',
        context={"objects": matching_series,
                 "type": "templos"}
    )

@user_is_superuser
def asignaciones(request):
    matching_series = Asignacion.objects.all()

    return render(
        request=request,
        template_name='main/lista.html',
        context={"objects": matching_series,
                 "type": "asignaciones"}
    )

@user_is_superuser
def paquetes(request):
    matching_series = Paquete.objects.all()

    return render(
        request=request,
        template_name='main/lista.html',
        context={"objects": matching_series,
                 "type": "paquetes"}
    )

#Espacio Trabajadores
@user_is_superuser
def trabajador(request, trabajador: str):
    matching_article = Trabajador.objects.filter(slug = trabajador).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article,
                           "type": "trabajador"}
    )

@user_is_superuser
def nuevo_trabajador(request):
    if request.method == 'POST':
        form = TrabajadoresCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trabajadores')
    else:
        form = TrabajadoresCreateForm()

    return render(
        request=request,
        template_name='main/nuevo_objeto.html',
        context={
            "object": "Trabajador",
            "form": form
            }
        )

@user_is_superuser
def trabajador_delete(request, trabajador: str):
    matching_article = Trabajador.objects.filter(slug = trabajador).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('trabajadores')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "trabajador"
                }
            )

@user_is_superuser
def trabajador_update(request, trabajador: str):
    matching_article = Trabajador.objects.filter(slug = trabajador).first()

    if request.method == "POST":
        form = TrabajadoresUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/trabajadores/{matching_article.slug}')
    
    else:
        form = TrabajadoresUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nuevo_objeto.html',
            context={
                "object": "Trabajador",
                "form": form,
                "type": "actualizar"
                }
            )
    
#Espacio Contratos
@user_is_superuser
def contrato(request, contrato: str):
    matching_article = Contrato.objects.filter(slug = contrato).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article,
                           "type": "contrato"}
    )

@user_is_superuser
def nuevo_contrato(request):
    if request.method == 'POST':
        form = ContratosCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contratos')
    else:
        form = ContratosCreateForm()

    return render(
        request=request,
        template_name='main/nuevo_objeto.html',
        context={
            "object": "Contrato",
            "form": form
            }
        )

@user_is_superuser
def contrato_delete(request, contrato: str):
    matching_article = Contrato.objects.filter(slug = contrato).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('contratos')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "contrato"
                }
            )

@user_is_superuser
def contrato_update(request, contrato: str):
    matching_article = Contrato.objects.filter(slug = contrato).first()

    if request.method == "POST":
        form = ContratosUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/contratos/{matching_article.slug}')
    
    else:
        form = ContratosUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nuevo_objeto.html',
            context={
                "object": "Contrato",
                "form": form,
                "type": "actualizar"
                }
            )    
    
#Espacio Ventas
@user_is_superuser
def venta(request, venta: str):
    matching_article = Venta.objects.filter(slug = venta).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article,
                           "type": "venta"}
    )

@user_is_superuser
def nuevo_venta(request):
    if request.method == 'POST':
        form = VentasCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ventas')
    else:
        form = VentasCreateForm()

    return render(
        request=request,
        template_name='main/nuevo_objeto.html',
        context={
            "object": "Venta",
            "form": form
            }
        )

@user_is_superuser
def venta_delete(request, venta: str):
    matching_article = Venta.objects.filter(slug = venta).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('ventas')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "venta"
                }
            )

@user_is_superuser
def venta_update(request, venta: str):
    matching_article = Venta.objects.filter(slug = venta).first()

    if request.method == "POST":
        form = VentasUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/ventas/{matching_article.slug}')
    
    else:
        form = VentasUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nuevo_objeto.html',
            context={
                "object": "Venta",
                "form": form,
                "type": "actualizar"
                }
            )  
    
#Espacio Asignaciones
@user_is_superuser
def asignacion(request, asignacion: str):
    matching_article = Asignacion.objects.filter(slug = asignacion).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article,
                           "type": "asignacion"}
    )

@user_is_superuser
def nuevo_asignacion(request):
    if request.method == 'POST':
        form = AsignacionesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('asignaciones')
    else:
        form = AsignacionesCreateForm()

    return render(
        request=request,
        template_name='main/nuevo_objeto.html',
        context={
            "object": "Asignacion",
            "form": form
            }
        )

@user_is_superuser
def asignacion_delete(request, asignacion: str):
    matching_article = Asignacion.objects.filter(slug = asignacion).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('asignaciones')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "asignacion"
                }
            )

@user_is_superuser
def asignacion_update(request, asignacion: str):
    matching_article = Asignacion.objects.filter(slug = asignacion).first()

    if request.method == "POST":
        form = AsignacionesUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/asignaciones/{matching_article.slug}')
    
    else:
        form = AsignacionesUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nuevo_objeto.html',
            context={
                "object": "Asignacion",
                "form": form,
                "type": "actualizar"
                }
            )  
    
#Espacio Salones
@user_is_superuser
def salon(request, salon: str):
    matching_article = Salon.objects.filter(slug = salon).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article,
                           "type": "salon"}
    )

@user_is_superuser
def nuevo_salon(request):
    if request.method == 'POST':
        form = SalonesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salones')
    else:
        form = SalonesCreateForm()

    return render(
        request=request,
        template_name='main/nuevo_objeto.html',
        context={
            "object": "Salon",
            "form": form
            }
        )

@user_is_superuser
def salon_delete(request, salon: str):
    matching_article = Salon.objects.filter(slug = salon).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('salones')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "salon"
                }
            )

@user_is_superuser
def salon_update(request, salon: str):
    matching_article = Asignacion.objects.filter(slug = salon).first()

    if request.method == "POST":
        form = SalonesUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/salones/{matching_article.slug}')
    
    else:
        form = SalonesUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nuevo_objeto.html',
            context={
                "object": "Salon",
                "form": form,
                "type": "actualizar"
                }
            )  
    
#Espacio Templo
@user_is_superuser
def templo(request, condicion: str):
    matching_article = templo.objects.filter(slug = condicion).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article,
                           "type": "templo"}
    )

@user_is_superuser
def nuevo_templo(request):
    if request.method == 'POST':
        form = TemplosCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('templos')
    else:
        form = TemplosCreateForm()

    return render(
        request=request,
        template_name='main/nuevo_objeto.html',
        context={
            "object": "Templo",
            "form": form
            }
        )

@user_is_superuser
def templo_delete(request, condicion: str):
    matching_article = Templo.objects.filter(slug = condicion).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('templos')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "templos"
                }
            )

@user_is_superuser
def templo_update(request, condicion: str):
    matching_article = Templo.objects.filter(slug = condicion).first()

    if request.method == "POST":
        form = TemplosUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/templos/{matching_article.slug}')
    
    else:
        form = TemplosUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nuevo_objeto.html',
            context={
                "object": "Templo",
                "form": form,
                "type": "actualizar"
                }
            )  
    
#Espacio Ubicaciones
@user_is_superuser
def ubicacion(request, filtro: str):
    matching_article = Ubicacion.objects.filter(slug = filtro).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article,
                           "type": "ubicacion"}
    )

@user_is_superuser
def nuevo_ubicacion(request):
    if request.method == 'POST':
        form = UbicacionesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ubicaciones')
    else:
        form = UbicacionesCreateForm()

    return render(
        request=request,
        template_name='main/nuevo_objeto.html',
        context={
            "object": "Ubicacion",
            "form": form
            }
        )

@user_is_superuser
def ubicacion_delete(request, ubicacion: str):
    matching_article = Ubicacion.objects.filter(slug = ubicacion).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('ubicaciones')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "ubicacion"
                }
            )

@user_is_superuser
def ubicacion_update(request, ubicacion: str):
    matching_article = Ubicacion.objects.filter(slug = ubicacion).first()

    if request.method == "POST":
        form = UbicacionesUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/ubicaciones/{matching_article.slug}')
    
    else:
        form = UbicacionesUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nuevo_objeto.html',
            context={
                "object": "Ubicacion",
                "form": form,
                "type": "actualizar"
                }
            )    

#Espacio Paquetes
@user_is_superuser
def paquete(request, paquete: str):
    matching_article = Paquete.objects.filter(slug = paquete).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article,
                           "type": "paquete"}
    )

@user_is_superuser
def nuevo_paquete(request):
    if request.method == 'POST':
        form = PaquetesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('paquetes')
    else:
        form = PaquetesCreateForm()

    return render(
        request=request,
        template_name='main/nuevo_objeto.html',
        context={
            "object": "Paquete",
            "form": form
            }
        )

@user_is_superuser
def paquete_delete(request, paquete: str):
    matching_article = Paquete.objects.filter(slug = paquete).first()

    if request.method == "POST":
        matching_article.delete()
        return redirect('paquetes')
    else:
        return render(
            request=request,
            template_name='main/confirm_delete.html',
            context={
                "object": matching_article,
                "type": "paquete"
                }
            )

@user_is_superuser
def paquete_update(request, paquete: str):
    matching_article = Paquete.objects.filter(slug = paquete).first()

    if request.method == "POST":
        form = PaquetesUpdateForm(request.POST, request.FILES, instance=matching_article)
        if form.is_valid():
            form.save()
            return redirect(f'/paquetes/{matching_article.slug}')
    
    else:
        form = PaquetesUpdateForm(instance=matching_article)

        return render(
            request=request,
            template_name='main/nuevo_objeto.html',
            context={
                "object": "Paquete",
                "form": form,
                "type": "actualizar"
                }
            )    