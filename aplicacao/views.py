# Databricks notebook source
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Cliente
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse


# Para criar um novo cliente
@method_decorator(csrf_exempt, name='dispatch')
class ClienteCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.create(**data)
            # Serializar os dados do cliente para o retorno
            cliente_data = {
                "id": cliente.id,
                "nome": cliente.nome,
                "cpf": cliente.cpf,
                "email": cliente.email,
                "telefone": cliente.telefone
            }
            return JsonResponse(cliente_data, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

# Para listar todos os clientes
@method_decorator(csrf_exempt, name='dispatch')            
class ClienteListView(View):
    def get(self, request):
        clientes = Cliente.objects.all()
        if not clientes:
            return JsonResponse({"message": "Sem clientes cadastrados."}, status=200)
        
        # Convertendo cada cliente em dicionário
        clientes_list = [model_to_dict(cliente) for cliente in clientes]
        return JsonResponse(clientes_list, safe=False, status=200)

# Para visualizar, atualizar e deletar um cliente específico
@method_decorator(csrf_exempt, name='dispatch')
class ClienteDetailView(View):
    def get(self, request, id):
        try:
            cliente = Cliente.objects.get(id=id)
            cliente_data = {"nome": cliente.nome, "cpf": cliente.cpf, "email": cliente.email, "telefone": cliente.telefone}
            return JsonResponse(cliente_data, status=200)
        except Cliente.DoesNotExist:
            return JsonResponse({"error": "Cliente não encontrado."}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class ClienteUpdateView(View):
    def put(self, request, id):
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.get(pk=id)
            for key, value in data.items():
                setattr(cliente, key, value)
            cliente.save()
            return JsonResponse(model_to_dict(cliente), safe=False, status=200)
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Cliente não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class ClienteDeleteView(View):
    def delete(self, request, id):
        try:
            cliente = Cliente.objects.get(pk=id)
            cliente.delete()
            return HttpResponse(status=204)
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Cliente não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
            
class HomeView(View):
    def get(self, request):
        return JsonResponse({"message": "Seja Bem Vindo - ApiRestFull Django"}, status=200)
