from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

    STATUS = [
        ('admin', 'administrador'),
        ('emp', 'empleado')
    ]
    nombre = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default='empleado')

    def __str__(self):
        return self.username