from django.contrib import admin
from django.urls import include, path
from .views import home

from . import views

urlpatterns = [
    path('', home),
    path('adicionar', views.adicionar, name="adicionar")


]
