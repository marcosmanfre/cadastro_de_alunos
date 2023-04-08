from django.contrib import admin
from django.urls import include, path

from . import views
from .views import home

urlpatterns = [
    path('', home),
    path('adicionar', views.home, name="adicionar")


]
