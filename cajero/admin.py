from django.contrib import admin
from .models import Producto, Venta, Arqueo
from admin_totals.admin import ModelAdminTotals
from django.db.models import Sum
from django.db.models.functions import Coalesce

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "unidad_medida", "precio", "cantidad", "created"]

class VentaAdmin(ModelAdminTotals):
    list_display = ["id", "id_user", "boleta", "total", "fecha"]
    list_totals = [("total", lambda field: Coalesce(Sum(field), 0))]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

class ArqueoAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha", "total"]

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Arqueo, ArqueoAdmin)