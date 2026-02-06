from cmath import e
from django.shortcuts import render
from django.http import FileResponse, Http404
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from geracao.models import *
from geracao.serializers import *
import cemig, cemig2, cemig3, cemig4, copel

# Create your views here.
class FaturamentosViewSet (ModelViewSet):
    #parser_classes = [MultiPartParser, FormParser]
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Faturamento.objects.all()
    serializer_class = FaturamentoSerializer
    def get_queryset(self):
        user = self.request.user
        print (user)
        faturamentos = Faturamento.objects.filter(usuario__exact=str(self.request.user)).order_by('-id')
        return faturamentos
    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperUser, ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()
    def perform_create(self, serializer):
        # Save with the new value for the target model fields
        serializer.save(usuario = self.request.user) 

class ClientesViewSet (ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    def get_queryset(self):
        user = self.request.user
        print (user)
        #return Cliente.objects.all()
        return Cliente.objects.filter(usuario__exact=str(self.request.user))
    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperUser, ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()
    def perform_create(self, serializer):
        # Save with the new value for the target model fields
        serializer.save(usuario = self.request.user)

@ api_view(['GET'])
def getFaturaPdf(request):
    id=request.query_params.get('id')
    faturamento = Faturamento.objects.filter(id__exact=id)[0]
    faturamento.imprimir_pdf()
    print (request.user)
    try:    
        filename = "invoice.pdf"
        return FileResponse(open(filename, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

@ api_view(['POST'])
def carregarConta(request):
    id=request.data['id']
    print (id)
    faturamento = Faturamento.objects.filter(id__exact=id)[0]
    #breakpoint()
    
    try:
        if (faturamento.distribuidora == 'cemig'):
            faturamento.carregarConta(pdf2txt=cemig.pdf2txt,
                    extrairPorte=cemig.extrairPorte,
                    extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
                    extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
                    extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
                    obterIluminacaoPublica=cemig.obterIluminacaoPublica,
                    extrairNumeroInstalacao=cemig.extrairNumeroInstalacao,
                    extrairReferencia=cemig.extrairReferencia,
                    extrairVencimento=cemig.extrairVencimento,
                    extrairSaldoResidual=cemig.extrairSaldoResidual)
        elif (faturamento.distribuidora=='copel'):
            faturamento.carregarConta(pdf2txt=copel.pdf2txt,
                    extrairPorte=copel.extrairPorte,
                    extrairHistoricoConsumo=copel.extrairHistoricoConsumo,
                    extrairEnergiaInjetada=copel.extrairEnergiaInjetada,
                    extrairCustoDisponibilidade=copel.extrairCustoDisponibilidade,
                    obterIluminacaoPublica=copel.obterIluminacaoPublica,
                    extrairNumeroInstalacao=copel.extrairNumeroInstalacao,
                    extrairReferencia=copel.extrairReferencia,
                    extrairVencimento=copel.extrairVencimento,
                    extrairSaldoResidual=copel.extrairSaldoResidual)
        elif (faturamento.distribuidora=='cemig2'):
            faturamento.carregarConta(pdf2txt=cemig2.pdf2txt,
                    extrairPorte=cemig2.extrairPorte,
                    extrairHistoricoConsumo=cemig2.extrairHistoricoConsumo,
                    extrairEnergiaInjetada=cemig2.extrairEnergiaInjetada,
                    extrairCustoDisponibilidade=cemig2.extrairCustoDisponibilidade,
                    obterIluminacaoPublica=cemig2.obterIluminacaoPublica,
                    extrairNumeroInstalacao=cemig2.extrairNumeroInstalacao,
                    extrairReferencia=cemig2.extrairReferencia,
                    extrairVencimento=cemig2.extrairVencimento,
                    extrairSaldoResidual=cemig2.extrairSaldoResidual)
        elif (faturamento.distribuidora=='cemig3'):
            faturamento.carregarConta(pdf2txt=cemig3.pdf2txt,
                    extrairPorte=cemig3.extrairPorte,
                    extrairHistoricoConsumo=cemig3.extrairHistoricoConsumo,
                    extrairEnergiaInjetada=cemig3.extrairEnergiaInjetada,
                    extrairCustoDisponibilidade=cemig3.extrairCustoDisponibilidade,
                    obterIluminacaoPublica=cemig3.obterIluminacaoPublica,
                    extrairNumeroInstalacao=cemig3.extrairNumeroInstalacao,
                    extrairReferencia=cemig3.extrairReferencia,
                    extrairVencimento=cemig3.extrairVencimento,
                    extrairSaldoResidual=cemig3.extrairSaldoResidual)
        elif (faturamento.distribuidora=='cemig4'):
            print ("Cheguei aqui 2!!!!")
            faturamento.carregarConta(pdf2txt=cemig4.pdf2txt,
                    extrairPorte=cemig4.extrairPorte,
                    extrairHistoricoConsumo=cemig4.extrairHistoricoConsumo,
                    extrairEnergiaInjetada=cemig4.extrairEnergiaInjetada,
                    extrairCustoDisponibilidade=cemig4.extrairCustoDisponibilidade,
                    obterIluminacaoPublica=cemig4.obterIluminacaoPublica,
                    extrairNumeroInstalacao=cemig4.extrairNumeroInstalacao,
                    extrairReferencia=cemig4.extrairReferencia,
                    extrairVencimento=cemig4.extrairVencimento,
                    extrairSaldoResidual=cemig4.extrairSaldoResidual)
        faturamento.save()
    except Exception as e:
        #Imprimir na tela o erro que veio na exceção, para ajudar a identificar o problema:

        print ("erro!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print (e)
        return Response({'Erro': 'Houve um problema ao carregar a conta. Certifique-se de que escolheu corretamente a distribuidora ou entre em contato com o desenvolvedor cwgestao@aol.com.'},
                 status=status.HTTP_400_BAD_REQUEST)

    print (faturamento.totalPagar)
    serializer =  FaturamentoSerializer(faturamento, many=False)
    return Response(serializer.data)

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
        return request.user and request.user.is_superuser


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                print (type(obj.usuario))
                print (type(str(request.user)))
                print (obj.usuario == str(request.user))
                return (obj.usuario == str(request.user))
        else:
            return False