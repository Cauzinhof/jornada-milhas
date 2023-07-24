from rest_framework import viewsets, status
from .models import Depoimento, Destino
from .serializer import DepoimentoSerializer, DestinoSerializer
import random
from rest_framework.response import Response


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
    serializer_class = DestinoSerializer

    def get_queryset(self):
        """
        Adiciona a possibilidade de filtrar o destino pelo nome
        a partir da url ?nome=<cidade>.
        Caso não seja passado argumento, todos os destinos 
        serão exibidos
        """
        queryset = Destino.objects.all()
        cidade = self.request.query_params.get('nome')
        if cidade is not None:
            queryset = queryset.filter(nome=cidade.title())
        return queryset
    
    def list(self, request, *args, **kwargs):
        """
        Redefinição da função list única e exclusivamente
        para retornar a mensagem personalidada e o 
        código 404.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if not queryset.exists():
            return Response({"mensagem":"Nenhum destino foi encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data)