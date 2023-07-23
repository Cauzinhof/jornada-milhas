from rest_framework import viewsets
from .models import Depoimento, Destino
from .serializer import DepoimentoSerializer, DestinoSerializer
import random

class DepoimentosViewSet(viewsets.ModelViewSet):
    """Listando todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer

class DepoimentosHomeViewSet(viewsets.ModelViewSet):
    """Exibindo aleatoriamente três depoimentos"""
    serializer_class = DepoimentoSerializer
    http_method_names = ['get']

    """Foi necessário sobrescrever a função a seguir pois apenas definir 
       o queryset não permite que os depoimentos sejam atualizados 
       a cada requisição pois ficam armazenados no cache"""
    def get_queryset(self):
        depoimentos = Depoimento.objects.all()
        #Escolha aleatória de 3 elementos. Necessário transformar em lista primeiro.
        queryset = random.sample(list(depoimentos), k=3)
        return queryset
    

class DestinosViewSet(viewsets.ModelViewSet):
    """Listando todos os destinos"""
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer