from django.urls import path
from anuncio.views import *

urlpatterns = [
    path('', ListaAnunciosView.as_view(), name='listar-anuncios'),
    path('novo/', CriarAnuncioView.as_view(), name='criar-anuncio'),
    path('<int:pk>/', AtualizarAnuncioView.as_view(), name='editar-anuncio'),
    path('deletar/<int:pk>/', ExcluirAnuncioView.as_view(), name='deletar-anuncio'),
]