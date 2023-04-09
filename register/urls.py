from django.contrib import admin
from django.urls import include, path

from . import views
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path('adicionar', views.adicionar, name="adicionar"),
    path('editar', views.editar, name='editar'),
    path('salvar/<str:id>', views.salvar, name='salvar'),
    path('deletar/<str:id>', views.deletar, name='deletar'),


]
