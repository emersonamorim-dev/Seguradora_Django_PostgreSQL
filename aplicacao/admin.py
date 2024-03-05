# Databricks notebook source
from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'telefone')  # Campos que você quer mostrar na listagem
    search_fields = ('nome', 'cpf')  # Campos pelo qual você quer permitir a busca
