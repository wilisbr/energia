from rest_framework import serializers
from geracao.models import *

class FaturamentoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Faturamento
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['endereco']=Faturamento.objects.filter(cpf_cliente=validated_data['cpf_cliente']).latest('id').endereco
        novo_faturamento=Faturamento.objects.create(**validated_data)
        return(novo_faturamento)

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'