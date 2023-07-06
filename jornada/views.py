from rest_framework import viewsets
from .models import Depoimento
from .serializer import DepoimentoSerializer

class DepoimentosViewSet(viewsets.ModelViewSet):
    """Listando todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer