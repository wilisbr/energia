from django.shortcuts import render
from django.http import FileResponse, Http404
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from geracao.models import *
from geracao.serializers import *
import cemig

# Create your views here.
class FaturamentosViewSet (ModelViewSet):
    #parser_classes = [MultiPartParser, FormParser]
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Faturamento.objects.all()
    serializer_class = FaturamentoSerializer
    def get_queryset(self):
        user = self.request.user
        print (user)
        return Faturamento.objects.filter(usuario__exact=str(self.request.user))
    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperUser, ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()


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
    faturamento.carregarConta(pdf2txt=cemig.pdf2txt,
            extrairPorte=cemig.extrairPorte,
            extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig.extrairNumeroInstalacao,
            extrairReferencia=cemig.extrairReferencia,
            extrairVencimento=cemig.extrairVencimento)
    faturamento.save()
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