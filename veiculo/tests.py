from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from anuncio.models import Veiculo
from veiculo.forms import *

# Create your tests here.

class TestesModelVeiculo(TestCase):
  def setUp(self):
    self.instancia = Veiculo(
      marca=1,
      modelo='ABCDE',
      ano=datetime.now().year,
      cor=2,
      combustivel=3
    )
  def text_is_new(self):
    self.assertTrue(self.instancia.veiculo_novo)
    self.instancia.ano = datetime.now().year - 5
    self.assertFalse(self.instancia.veiculo_novo)

  def test_years_use(self):
    self.instancia.ano = datetime.now().year - 10
    self.assertEqual(self.instancia.anos_de_uso(), 10)

class TestesViewListarVeiculos(TestCase):
  def setUp(self):
    self.user = User.objects.create(username='teste', password='12345')
    self.client.force_login(self.user)
    self.url = reverse('listar-veiculos')
    Veiculo(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4).save()
  
  def test_get(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.context.get('veiculos')), 1)

class TestesViewCriarVeiculo (TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculos')
    
    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
    
    def test_post(self):
          data = {
              'marca': 1,
              'modelo': 'Fusca',
              'ano': datetime.now().year,
              'cor': 2,
              'combustivel': 1
          }
          response = self.client.post(self.url, data)

          self.assertEqual(response.status_code, 302)
          self.assertRedirects(response, reverse('listar-veiculos'))

          self.assertEqual(Veiculo.objects.count(), 1)
          self.assertEqual(Veiculo.objects.first().modelo, 'Fusca')

class TestesViewEditarVeiculos(TestCase):
   
   def setUp(self):
      self.user = User.objects.create(username='teste',password='12345')
      self.client.force_login(self.user)
      self.instancia = Veiculo.objects.create(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4)
      self.url = reverse('editar-veiculos', kwargs={'pk': self.instancia.pk})

   def test_get(self):
      response = self.client.get(self.url)
      self.assertEqual(response.status_code, 200)
      self.assertIsInstance(response.context.get('object'), Veiculo)
      self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
      self.assertEqual(response.context.get('object').pk, self.instancia.pk)
      self.assertEqual(response.context.get('object').marca, 1)

   def test_post(self):
      data = {'marca': 5, 'modelo': 'FGHIJ', 'ano':4, 'cor':2, 'combustivel':1}
      response = self.client.post(self.url, data)
      self.assertEqual(response.status_code, 302)
      self.assertRedirects(response, reverse('listar-veiculos'))
      self.assertEqual(Veiculo.objects.count(),1)
      self.assertEqual(Veiculo.objects.first().marca,5)
      self.assertEqual(Veiculo.objects.first().pk, self.instancia.pk)

class TestesViewDeletarVeiculos(TestCase):
   def setUp(self):
      self.user = User.objects.create(username='teste', password='12345')
      self.client.force_login(self.user)
      self.instancia = Veiculo.objects.create(marca=1, modelo='ABCDE', ano=2, cor=3, combustivel=4)
      self.url = reverse('deletar-veiculos', kwargs={'pk': self.instancia.pk}) 
    
   def test_get(self):
      response = self.client.get(self.url)
      self.assertEqual(response.status_code, 200)
      self.assertIsInstance(response.context.get('object'), Veiculo)
      self.assertEqual(response.context.get('object').pk, self.instancia.pk)

   def test_post(self):
      response = self.client.post(self.url)

      self.assertEqual(response.status_code, 302)
      self.assertRedirects(response, reverse('listar-veiculos'))
      self.assertEqual(Veiculo.objects.count(), 0)