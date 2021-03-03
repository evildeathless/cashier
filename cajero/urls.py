from django.urls import path
from .views import home, login, productos, ventas

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('productos/', productos, name="productos"),
    path('venta/<id>', ventas, name="ventas")
]