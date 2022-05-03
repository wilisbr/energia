from django.db import models
import PyPDF2
import numpy as np
import math
import os, sys, inspect

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, currentdir)
import cemig

franquiaOficial = {'Trifásico': 100, 'Bifásico': 50, 'Monofásico': 30}
DJANGO_SETTINGS_MODULE = '..\gestaoEnergia\settings.py'


# Create your models here.
class Cliente(models.Model):
    """
    Essa classe representa um cliente que compra a energia do gerador
    
    Attributes
    ----------
    cpf: int
        CPF do cliente.
    
    """
    cpf_cliente = models.IntegerField()

    def gravar(self):
        self.save()

class Faturamento(models.Model):
    """
    Essa classe representa uma fatura mensal de energia.

    ...
    Attributes
    ----------
    conta_pdf: file
        Arquivo PDF contendo a conta.
    bonus : decimal
        Bônus de cortesia que foi dado pelo gerador ao cliente
    consumoSimulado : decimal
        Quantidade de kwh consumidor da distribuidora, caso não houvesse energia injetada na instalação
    custo_disponibilidade : decimal
        Tarifa mínima que foi cobrada na conta, pela distribuidora
    consumo_mes : decimal
        Consumo de energia, em kwh
    desconto: decimal
        Desconto (em percentual) sob o preço da concessionária: 
        ex: para 10% de desconto, deve ser preenchido 10
    energia_da_concessionaria:
        Energia injetada pela concessionária, em kwh (inclusive aquela decorrente do pagamento do custo disponibilidade, se for o caso)
    franquia : decimal
        Quantidade de kwh que a distruibuidora creditou por conta do custo de disponibilidade que foi cobrado
        Nem sempra CEMIG credita esse valor. Aparentemente, quando o intervalo entre leituras é menor que 30 dias,
        não é creditado nada.
    iluminacaoPublica : decimal
        Valor cobrado pela prefeitura a título de iluminação pública
    injetada : decimal
        Quantidade injetada na conta do cliente, em khw
    porte : str
        Pode ser Monofásico, Bifásico ou Trifásico
    tarifa : decimal
        Tarifa cobrada pela distribuidora, em R$ por kwh
    tarifaInjetada : decimal
        Tarifa cobrada do cliente pelo gerador, em R$/kwh (padrão é dar um desconto de 20% a 30% em cima da tarifa oficial)
    totalSimulado : decimal
        Valor da conta de luz caso não houvesse energia injetada na instalação
        valorConsumoSimulado + iluminacaoPublica
    totalPagar : decimal
        Total que o cliente deve pagar ao fornecedor, considerando que o fornecedor já quitou a conta da distribuidora
        iluminacaoPublica + custo_disponibilidade + valorInjetado - bonus
    valorConsumoSimulado : decimal
        Valor, em R$, correspondente ao consumo de energia da fatura, caso não houvesse injeção de energia fotovoltáica
        tarifa * consumo_mes
    valorInjetado : decimal
        Valor referente à quantidade de kwh injetada na instalação do cliente. 
        tarifaInjetada * injetada
    usuario : str 
        Nome do usuario da plataforma que cadastrou a fatura
    cpf_cliente : Int
        CPF do cliente que compra a energia

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    conta_pdf = models.FileField(upload_to='contas_pdf', null=True, blank=True)
    desconto = models.DecimalField(decimal_places=2,
                                   max_digits=10,
                                   null=False,
                                   blank=False,
                                   default=0)
    bonus = models.DecimalField(decimal_places=2,
                                max_digits=10,
                                null=False,
                                blank=False,
                                default=0)
    consumoSimulado = models.DecimalField(decimal_places=2,
                                          max_digits=10,
                                          null=True,
                                          blank=True)
    custo_disponibilidade = models.DecimalField(decimal_places=2,
                                                max_digits=10,
                                                null=True,
                                                blank=True)

    consumo_mes = models.DecimalField(decimal_places=2,
                                      max_digits=10,
                                      null=True,
                                      blank=True)
    energia_da_concessionaria = models.DecimalField(decimal_places=2,
                                                    max_digits=10,
                                                    null=True,
                                                    blank=True)
    franquia = models.DecimalField(decimal_places=2,
                                   max_digits=10,
                                   null=True,
                                   blank=True)
    iluminacaoPublica = models.DecimalField(decimal_places=2,
                                            max_digits=10,
                                            null=True,
                                            blank=True)
    injetada = models.DecimalField(decimal_places=2,
                                   max_digits=10,
                                   null=True,
                                   blank=True)
    porte = models.CharField(max_length=15, null=True, blank=True)
    tarifa = models.DecimalField(decimal_places=2,
                                 max_digits=10,
                                 null=True,
                                 blank=True)
    tarifaInjetada = models.DecimalField(decimal_places=2,
                                         max_digits=10,
                                         null=True,
                                         blank=True)
    totalSimulado = models.DecimalField(decimal_places=2,
                                        max_digits=10,
                                        null=True,
                                        blank=True)
    totalPagar = models.DecimalField(decimal_places=2,
                                     max_digits=10,
                                     null=True,
                                     blank=True)
    valorConsumoSimulado = models.DecimalField(decimal_places=2,
                                               max_digits=10,
                                               null=True,
                                               blank=True)
    valorInjetado = models.DecimalField(decimal_places=2,
                                        max_digits=10,
                                        null=True,
                                        blank=True)

    usuario = models.CharField(max_length=40, null=True, blank=True)
    cpf_cliente = models.ForeignKey(Cliente, models.SET_NULL,
        blank=True,
        null=True)

    def carregarConta(self, *args, **kwargs):
        '''
        Carrega uma conta de energia no objeto, extraindo do PDF os valores e armzenando-os nos atributos.

        ----------
        Parâmetros:
        conta_pdf: str 
            caminho do arquivo pdf da conta de luz
        desconto: float 
            valor do desconto concedido na tarifa, em relação ao preço da CEMIG
        bonus: float 
            que será creditado na conta
        pdf2txt: função
            parâmetro: string com o caminho do arquivo PDF
            saída: string com a conta convertida para texto
        extrairPorte: função
            parâmetro: string que contém a conta de energia
            saída: string contendo o porte da instalação, que pode ser "Monofásico", "Bifásico" ou "Trifásico"
        extrairHistoricoConsumo: função
            parâmetro: string que contém a conta de energia
            saída: float[] contendo o histórico de consumo
        extrairEnergiaInjetada: função
            parâmetro: string que contém a conta de energia
            saída: float com a quantidade de energia injetada pelo gerador
        extrairCustoDisponibilidade: função
            parâmetro: string que contém a conta de energia
            saída: float contendo o custo de disponibilidade
        obterIluminacaoPublica: função
            parâmetro: string que contém a conta de energia
            saída: float contendo o valor cobrado pela iluminação pública

        ----------
        Atributos atualizados pelo método:
        conta_pdf
        consumo_mes
        desconto
        bonus
        porte
        injetada
        custo_disponibilidade
        iluminacaoPublica
        tarifa
        ----------

        '''
        pdf2txt = kwargs.get('pdf2txt', False)
        extrairPorte = kwargs.get('extrairPorte', False)
        extrairHistoricoConsumo = kwargs.get('extrairHistoricoConsumo', False)
        extrairEnergiaInjetada = kwargs.get('extrairEnergiaInjetada', False)
        extrairCustoDisponibilidade = kwargs.get('extrairCustoDisponibilidade',
                                                 False)
        obterIluminacaoPublica = kwargs.get('obterIluminacaoPublica', False)

        if (kwargs.get('conta_pdf') == None):
            print('Necessário informar o parâmetro "conta"')
            return None

        self.conta_pdf = kwargs.get('conta_pdf')
        self.desconto = kwargs.get('desconto', 0)
        self.bonus = kwargs.get('bonus', 0)

        conta_txt = pdf2txt(self.conta_pdf.path, 0)

        self.porte = extrairPorte(conta_txt)

        self.injetada = extrairEnergiaInjetada(conta_txt)
        self.custo_disponibilidade = extrairCustoDisponibilidade(conta_txt)[0]
        self.energia_da_concessionaria = extrairCustoDisponibilidade(
            conta_txt)[1]
        self.tarifa = extrairCustoDisponibilidade(conta_txt)[2]
        self.iluminacaoPublica = obterIluminacaoPublica(conta_txt)
        consumos_mensais = extrairHistoricoConsumo(conta_txt)
        self.consumo_mes = consumos_mensais[0]

        self.tarifa = self.custo_disponibilidade / franquiaOficial[
            self.porte] if math.isnan(self.tarifa) else self.tarifa

        self.calcularFaturaSemEnergiaFotovoltaica()
        self.calcularFaturaComEnergiaFotovoltaica()

    def calcularFaturaComEnergiaFotovoltaica(self, *args, **kwargs):
        '''
        Calcula os atributos que dizem respeito à conta a ser paga para o gerador de energia fotovoltaica.
        Os atributos são armazenados no objeto.

        ----------
        Parâmetro: nenhum
        ----------
        Saída: nenhuma
        ----------
        Atributos atualizados pelo método:
        franquia
        tarifa
        tarifaInjetada
        valorInjetado
        totalPagar
        ----------

        '''
        self.franquia = self.consumo_mes - self.injetada

        #Tarifa cobrada do cliente, com o desconto definido
        self.tarifaInjetada = ((100 - self.desconto)/100) * self.tarifa

        #Valor que será cobrado do cliente pela energia injetada
        self.valorInjetado = self.tarifaInjetada * self.injetada

        self.totalPagar = self.iluminacaoPublica + self.custo_disponibilidade + self.valorInjetado - self.bonus

    def calcularFaturaSemEnergiaFotovoltaica(self, *args, **kwargs):
        '''
        Calcula os atributos que dizem respeito à conta aque seria paga à distribuidora, caso não houvesse energia injetada.
        Os atributos são armazenados no objeto.

        ----------
        Parâmetro: nenhum
        ----------
        Saída: nenhuma
        ----------
        Atributos atualizados pelo método:
        tarifa
        valorConsumoSimulado
        totalSimulado
        ----------

        '''

        self.valorConsumoSimulado = float(self.consumo_mes) * self.tarifa
        self.valorConsumoSimulado = franquiaOficial[
            self.porte] if self.valorConsumoSimulado < franquiaOficial[
                self.
                porte] else self.valorConsumoSimulado  #Caso o consumo seja menor que a franquia, colocar a franquia como consumo simulado

        self.totalSimulado = self.valorConsumoSimulado + self.iluminacaoPublica

    def imprimir(self):
        '''
        Esse método apenas imprime alguns atributos, permitindo ao usuário comparar as duas contas.

        '''
        print('---------------Conta atual (com desconto)-------------')
        print('Tarifa da energia injetada: ' + str(self.tarifaInjetada))
        print('Energia injetada (kw/h): ' + str(self.injetada) + '   R$: ' +
              str(self.valorInjetado))
        print('Iluminação pública: ' + str(self.iluminacaoPublica))
        print('Franquia Cemig: ' + str(self.franquia))
        print('Custo de disponibilidade: ' + str(self.custo_disponibilidade))
        print('Bônus cortesia: -' + str(self.bonus))
        print('Total a pagar: R$ ' + str(self.totalPagar))
        print('------------------------------------------------------\n\n')

        print('---------Simulação SEM energia fotovoltaica-----------')
        print('Tarifa CEMIG: ' + str(self.tarifa))
        print('Consumo simulado: ' + str(self.valorConsumoSimulado))
        print('Iluminação pública: ' + str(self.iluminacaoPublica))
        print('Total da conta simulada: R$ ' + str(self.totalSimulado))
        print('------------------------------------------------------\n\n')

        economia = self.totalSimulado - self.totalPagar
        economiaPercentual = 100 * economia / self.totalSimulado
        print('Economia de R$ ' + str(economia) + ' = ' +
              str(economiaPercentual) + '%')

    def gravar(self):
        self.save()
    
    def save(self, *args, **kwargs):
        print ('Salvando e alterando o objeto Faturamento')
        self.carregarConta(
            conta_pdf='geracao/tests/noname.pdf',
            pdf2txt=cemig.pdf2txt,
            extrairPorte=cemig.extrairPorte,
            extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig.obterIluminacaoPublica,
            desconto=0.2,
            bonus=30)
        super().save(*args, **kwargs)
