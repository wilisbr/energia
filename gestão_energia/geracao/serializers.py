from rest_framework import serializers
from geracao.models import *

class FaturamentoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Faturamento
        fields = '__all__'