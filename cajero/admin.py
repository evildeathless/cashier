from django.contrib import admin
from .models import Producto, Venta, Arqueo

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "unidad_medida", "precio", "cantidad", "created"]

class VentaAdmin(admin.ModelAdmin):
    list_display = ["id", "id_user", "boleta", "total", "fecha"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

class ArqueoAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha", "total"]

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Arqueo, ArqueoAdmin)