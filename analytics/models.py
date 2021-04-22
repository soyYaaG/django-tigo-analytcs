"""Anlytics Models"""

# django
from django.db import models


class TestUser(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    edad = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'test_user'