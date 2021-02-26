from django.urls import path
from .views import home, login, productos

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('productos/', productos, name="productos")
]