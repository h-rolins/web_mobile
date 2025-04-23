from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

class Login (View):
    def get (self, request):
        contexto = {'mensagem': 'teste 001'}
        if request.user.is_authenticated:
            return redirect("/veiculo")
        else:
            return render(request,'autentificacao.html',contexto)

    def post (self, request):
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect ("/veiculo")
            return render (request, 'autentificacao.html')
        usuario = request.POST.get('usuario',None)
        senha = request.POST.get('senha',None)

        print(usuario)
        print(senha)

class Logout (View):
    def get(self, request):
        logout(request)
        return redirect (settings.LOGIN_URL)