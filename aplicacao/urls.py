# Databricks notebook source
from django.urls import path
from .views import ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDeleteView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),  # GET para listar clientes
    path('clientes/new/', ClienteCreateView.as_view(), name='cliente_create'),  # POST para criar um novo cliente
    path('clientes/<int:id>/update/', ClienteUpdateView.as_view(), name='cliente_update'),  # PUT para atualizar um cliente
    path('clientes/<int:id>/delete/', ClienteDeleteView.as_view(), name='cliente_delete'),  # DELETE para excluir um cliente
]

