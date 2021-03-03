from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Venta

# Create your views here.
def home(request):
    return render(request, 'cajero/home.html')

def login(request):
    return render(request, 'cajero/login.html')

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'cajero/productos.html', data)

def ventas(request, id):
    producto = get_object_or_404(Producto, id = id)
    data = {
        'p':producto
    }
    return render(request, 'cajero/ventas.html', data)