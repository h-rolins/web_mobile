from django.shortcuts import render
from veiculo.models import Veiculo
from django.views.generic import View
from django.urls import reverse_lazy
from veiculo.forms import FormularioVeiculo
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class ListarVeiculos(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class CriarVeiculos (LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class EditarVeiculos (LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy ('listar-veiculos')

class DeletarVeiculos (LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy ('listar-veiculos')

class FotoVeiculo (View):
    def get (self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get (foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse (veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404 ("Foto não encontrada ou acesso não autorizado")
        except Exception as exception:
            raise exception 