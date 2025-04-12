from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

def index (request):
    return HttpResponse ("Sistema para gerenciamentro de veículos")

class Login (View):
    def get (self, request):
        contexto = {'mensagem': 'teste 001'}
        return render(request,'autentificacao.html',contexto)