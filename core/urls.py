from django.contrib import admin
from django.urls import path, include
from .views import areaAdmin, delete, editar, home, salvar, update

urlpatterns = [
    path("", home),
    path("areaAdmin/", areaAdmin, name="areaAdmin"),
    path("salvar/", salvar, name="salvar"),
    path("editar/<int:id>", editar, name="editar"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", delete, name="delete"),
]