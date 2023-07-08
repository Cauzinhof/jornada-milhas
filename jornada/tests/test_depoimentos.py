from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from ..models import Depoimento
from ..serializer import DepoimentoSerializer

class VerificaRequisicoesTestCase(APITestCase):
    def setUp(self) -> None:
        self.depoimentos_url = reverse('Depoimentos-list')
        self.depoimento = Depoimento.objects.create(
            nome= 'Nome Teste 12',
            depoimento= 'Esse é um depoimento teste apenas para testar depoimentos',
            foto='teste'
        )
        self.serializer = DepoimentoSerializer(instance=self.depoimento)
        #Cria a url do objeto criado acima, para os testes PUT e DELETE
        self.objeto_url = reverse('Depoimentos-list') + f'{self.depoimento.id}/'

    def test_verifica_status_da_requisicao_get(self):
        """Verifica se é possível fazer uma requisição GET"""
        response = self.client.get(self.depoimentos_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_verifica_status_da_requisicao_post(self):
        """Verifica se é possível fazer uma requisição POST"""
        data = {
            'nome': 'Nome Teste 2',
            'depoimento': 'Esse é um depoimento teste apenas para testar depoimentos',
            'foto': ''
        }
        response = self.client.post(path=self.depoimentos_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_status_da_requisicao_put(self):
        """Verifica se é possível fazer uma requisição PUT"""
        data = {
            "id" : self.depoimento.id,
            "nome": "Nome Teste PUT",
            "depoimento": "Esse é um depoimento teste apenas para testar depoimentos",
            "foto": ""
        }
        response = self.client.patch(path=self.objeto_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_status_da_requisicao_delete(self):
        """Verifica se é possível fazer uma requisição DELETE"""
        response = self.client.delete(path=self.objeto_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


