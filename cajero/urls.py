from django.urls import path
from .views import home, login, productos, ventas, agregar_venta

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('productos/', productos, name="productos"),
    path('ventas/', ventas, name="ventas"),
    path('agregar-producto', agregar_venta, name="add")
]