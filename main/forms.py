from django import forms
from .models import *

class TrabajadoresCreateForm(forms.ModelForm):
    class Meta:
        model = Trabajador

        fields = [
            "nombre_empleado",
            "tipo_trabajo",
            "empleado_activo",
        ]

class TrabajadoresUpdateForm(forms.ModelForm):
    class Meta:
        model = Trabajador

        fields = [
            "nombre_empleado",
            "tipo_trabajo",
            "empleado_activo",
        ]

#Contratos
class ContratosCreateForm(forms.ModelForm):
    class Meta:
        model = Contrato

        fields = [
            "paquete_contrato",
            "nombre_cliente_contrato",
            "fecha_contrato",
            "lugar_contrato",
            "templo_contrato",
            "salon_contrato",
            "tipo_evento_contrato",
            "hora_contrato",
            "nota_contrato",
            "contrato_activo",
        ]

class ContratosUpdateForm(forms.ModelForm):
    class Meta:
        model = Contrato

        fields = [
            "paquete_contrato",
            "nombre_cliente_contrato",
            "fecha_contrato",
            "lugar_contrato",
            "templo_contrato",
            "salon_contrato",
            "tipo_evento_contrato",
            "hora_contrato",
            "nota_contrato",
            "contrato_activo",
        ]

#Asignaciones
class AsignacionesCreateForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        
        contrato_asignado = forms.ModelChoiceField(queryset=Contrato.objects.filter(contrato_activo=True))
        
        fields = [
            "contrato_asignado",
            "empleado_asignado",
            "tipo_asignacion",
        ]

class AsignacionesUpdateForm(forms.ModelForm):
    class Meta:
        model = Asignacion

        fields = [
            "contrato_asignado",
            "empleado_asignado",
            "tipo_asignacion",
        ]

#Paquetes
class PaquetesCreateForm(forms.ModelForm):
    class Meta:
        model = Paquete

        fields = [
            "nombre_paquete",
            "descripcion_paquete",
            "precio_paquete",
        ]

class PaquetesUpdateForm(forms.ModelForm):
    class Meta:
        model = Paquete

        fields = [
            "nombre_paquete",
            "descripcion_paquete",
            "precio_paquete",
        ]

#Salones
class SalonesCreateForm(forms.ModelForm):
    class Meta:
        model = Salon

        fields = [
            "nombre_salon",
            "ubicacion_salon",
        ]

class SalonesUpdateForm(forms.ModelForm):
    class Meta:
        model = Salon

        fields = [
            "nombre_salon",
            "ubicacion_salon",
        ]

#Templos        
class TemplosCreateForm(forms.ModelForm):
    class Meta:
        model = Templo

        fields = [
            "nombre_templo",
            "ubicacion_templo",
        ]

class TemplosUpdateForm(forms.ModelForm):
    class Meta:
        model = Templo

        fields = [
            "nombre_templo",
            "ubicacion_templo",
        ]

#Ubicacion
class UbicacionesCreateForm(forms.ModelForm):
    class Meta:
        model = Ubicacion

        fields = [
            "nombre_ubicacion",
            "tipo_ubicacion",
        ]

class UbicacionesUpdateForm(forms.ModelForm):
    class Meta:
        model = Ubicacion

        fields = [
            "nombre_ubicacion",
            "tipo_ubicacion",
        ]

#Ventas
class VentasCreateForm(forms.ModelForm):
    class Meta:
        model = Venta

        fields = [
            "paquete_venta",
            "usuario_venta",
            "total_venta",
        ]

class VentasUpdateForm(forms.ModelForm):
    class Meta:
        model = Venta

        fields = [
            "paquete_venta",
            "usuario_venta",
            "total_venta",
        ]