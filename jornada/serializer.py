from rest_framework import serializers
from .models import Depoimento, Destino

class DepoimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Depoimento
        fields = '__all__'

class DestinoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destino
        fields = ['foto_1', 'foto_2', 'nome', 'meta', 'texto_descritivo']