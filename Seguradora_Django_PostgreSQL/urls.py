# Databricks notebook source
from django.contrib import admin
from django.urls import path, include
from aplicacao.views import HomeView  # Certifique-se de importar HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('aplicacao.urls')),  # Inclui as URLs da aplicação `aplicacao`
    path('', HomeView.as_view(), name='home'),  # Rota para a HomeView na raiz
]
