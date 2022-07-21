from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def produtosLoja(request):
    return HttpResponse('Teste')

def listaProdutos(request):
    return render(request, 'produtos/list.html')