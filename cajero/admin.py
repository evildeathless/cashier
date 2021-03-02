from django.contrib import admin
from .models import Producto, Venta

# Register your models here.
admin.site.register(Producto)
admin.site.register(Venta)