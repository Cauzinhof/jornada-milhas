from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..serializer import DestinoSerializer
from ..models import Destino

class VerificaRequisicoesTestCase(APITestCase):
    def setUp(self) -> None:
        self.destinos_url = reverse("Destinos-list")
        self.destino = Destino.objects.create(
            nome= 'Destino teste',
            preco= 'R$ 2.500,00',
            foto='teste'
        )
        self.serializer = DestinoSerializer(instance=self.destino)
        self.objeto_url = reverse('Destinos-list') + f'{self.destino.id}/'
    
    def test_verifica_status_da_requisicao_get_destinos(self):
        """Verifica se é possível fazer uma requisição GET"""
        response = self.client.get(self.destinos_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_status_da_requisicao_post_destinos(self):
        """Verifica se é possível fazer uma requisição POST"""
        data = {
            'nome': 'Lugar teste',
            'preco': 'R$ 1.000,00',
            'foto': ''
        }
        response = self.client.post(path=self.destinos_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_verifica_status_da_requisicao_put_destinos(self):
        """Verifica se é possível fazer uma requisição PUT"""
        data = {
            "id" : self.destino.id,
            "nome": "Nome Teste PUT",
            "preco": "R$ 1.000,00",
            "foto": ""
        }
        response = self.client.put(path=self.objeto_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_status_da_requisicao_delete_destinos(self):
        """Verifica se é possível fazer uma requisição DELETE"""
        response = self.client.delete(path=self.objeto_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)