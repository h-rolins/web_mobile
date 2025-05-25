from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Anuncio
from django.urls import reverse_lazy
from anuncio.forms import FormularioAnuncio
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaAnunciosView(ListView):
    model = Anuncio
    template_name = 'anuncio/listar.html'
    context_object_name = 'anuncios'
    queryset = Anuncio.objects.filter(ativo=True).order_by('-criado_em')

class CriarAnuncioView(LoginRequiredMixin, CreateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')

    def form_valid(self, form):
        form.instance.anunciante = self.request.user  # define o anunciante
        return super().form_valid(form)

class AtualizarAnuncioView(LoginRequiredMixin, UpdateView):
    model = Anuncio
    fields = ['titulo', 'descricao', 'preco', 'ativo', 'veiculo']
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios')

class ExcluirAnuncioView(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')