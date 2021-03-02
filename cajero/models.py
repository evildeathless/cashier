from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal
from django.conf import settings

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=12)
    nombre = models.CharField(max_length=15)
    unidad_medida = models.CharField(max_length=10)
    precio = models.DecimalField(null=False, validators=[MinValueValidator(Decimal('0.01'))], max_digits=7, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos", null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    precio = models.DecimalField(null=False, validators=[MinValueValidator(Decimal('0.01'))], max_digits=7, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)