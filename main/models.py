from django.db import models
from django.utils import timezone

# Create your models here.
class Trabajador(models.Model):
    nombre_empleado = models.CharField(max_length=30, primary_key=True)
    tipos_trabajo = [
        ('Foto', 'Fotógrafo'),
        ('Vídeo', 'Vídeo'),
        ('Mostrador', 'Mostrador')
    ]
    tipo_trabajo = models.CharField(max_length=100, choices=tipos_trabajo, default='F')
    empleado_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_empleado
    
    class Meta:
        verbose_name_plural = "Trabajadores"

class Paquete(models.Model):
    codigo_paquete = models.AutoField(primary_key=True)
    nombre_paquete = models.CharField(max_length=30)
    descripcion_paquete = models.CharField(max_length=255)
    precio_paquete = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0}, incluye {1}, precio: ${2}.00"
        return txt.format(self.nombre_paquete, self.descripcion_paquete, self.precio_paquete)
    
    class Meta:
        verbose_name_plural = "Paquetes"

class Ubicacion(models.Model):
    codigo_ubicacion = models.AutoField(primary_key=True)
    nombre_ubicacion = models.CharField(max_length=30)
    tipos_ubicacion = [
        ('A', 'Acámbaro'),
        ('R', 'Rancho')
    ]
    tipo_ubicacion = models.CharField(max_length=1, choices=tipos_ubicacion, default='A')

    def __str__(self):
        return self.nombre_ubicacion
    
    class Meta:
        verbose_name_plural = "Ubicaciones"

class Salon(models.Model):
    codigo_salon = models.AutoField(primary_key=True)
    nombre_salon = models.CharField(max_length=30)
    ubicacion_salon = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre_salon)
    
    class Meta:
        verbose_name_plural = "Salones"

class Templo(models.Model):
    codigo_templo = models.AutoField(primary_key=True)
    nombre_templo = models.CharField(max_length=30)
    ubicacion_templo = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre_templo)

class Contrato(models.Model):
    folio_contrato = models.AutoField(primary_key=True)
    paquete_contrato = models.ForeignKey(Paquete, null=False, blank=False, on_delete=models.CASCADE)
    nombre_cliente_contrato = models.CharField(max_length=100)
    fecha_contrato = models.DateField()
    lugar_contrato = models.ForeignKey(Ubicacion, null=False, blank=False, on_delete=models.CASCADE)
    templo_contrato = models.ForeignKey(Templo, null=False, blank=False, on_delete=models.CASCADE)
    salon_contrato = models.ForeignKey(Salon, null=False, blank=False, on_delete=models.CASCADE)
    tipo_evento_contrato = models.CharField(max_length=50)
    hora_contrato = models.CharField(max_length=10)
    nota_contrato = models.TextField()
    contrato_activo = models.BooleanField(default=True)

    def __str__(self):
        txt = "{0} | {1} - Paquete: {2} misa en: {3}, en salón: {4}, el evento es: {5}, a nombre de: {6}, el día {7} a las {8} NOTA: {9}"
        if self.contrato_activo:
            activo = "VIGENTE"
        else:
            activo = "PASADO"
        return txt.format(activo, self.folio_contrato, self.paquete_contrato, self.templo_contrato, self.salon_contrato, self.tipo_evento_contrato, self.nombre_cliente_contrato, self.fecha_contrato, self.hora_contrato, self.nota_contrato)

class Venta(models.Model):
    folio_venta = models.AutoField(primary_key=True)
    paquete_venta = models.ForeignKey(Paquete, null=False, blank=False, on_delete=models.CASCADE)
    usuario_venta = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total_venta = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} - Venta de {1}, hecha por {2}, el día {3}, con un total de ${4}.00"
        return txt.format(self.folio_venta, self.paquete_venta, self.usuario_venta, self.total_venta)

class Asignacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    contrato_asignado = models.ForeignKey(Contrato, null=False, blank=False, on_delete=models.CASCADE)
    empleado_asignado = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    tipos_asignacion = [
        ('Fotos', 'Fotógrafo'),
        ('Vídeo', 'Vídeo'),
        ('Sesión', 'Sesión')
    ]
    tipo_asignacion = models.CharField(max_length=100, choices=tipos_asignacion, default='F')

    def __str__(self):
        txt = "{0} asignado como {1} a {2}"
        return txt.format(self.empleado_asignado, self.tipo_asignacion, self.contrato_asignado)
    
    class Meta:
        verbose_name_plural = "Asignaciones"