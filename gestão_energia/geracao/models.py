from django.db import models
import PyPDF2
from django.forms import EmailField
import numpy as np
import math
import os, sys, inspect
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.lib.colors import Color
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    cpf_cliente: int
        CPF do cliente.
    nome: string
        Nome do cliente
    telefone: string
        Telefone do cliente
    usuario : str 
        Nome do usuario da plataforma que cadastrou o cliente
    
    """
    cpf_cliente = models.IntegerField()
    usuario= models.CharField(max_length=40, null=True, blank=True)
    nome = models.TextField(null=False, blank=False)
    telefone = models.TextField(null=True, blank=True)

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
    economia_valor : decimal
        Valor economizado pelo cliente
    economia_percentual : decimal
        Percentual economizado pelo cliente. Armazenar apenas o número. 
        Ex: para 10,4%, armazenar o valor 10.4
    endereco: string
        Endereço da instalação
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
    instalacao: int
        Número da instalação
    porte : str
        Pode ser Monofásico, Bifásico ou Trifásico
    referencia: str
        Mês/ano de referência da fatura MMM/AAAA (ex: ABR/2022)
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
    vencimento: str
        Dia/Mês/ano de vencimento da fatura DD/MM/AAAA (ex: 11/05/2022)
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
    desconto = models.FloatField(
                                   null=False,
                                   blank=False,
                                   default=0)
    bonus = models.FloatField(
                                null=False,
                                blank=False,
                                default=0)
    consumoSimulado = models.FloatField(
                                          null=True,
                                          blank=True)
    custo_disponibilidade = models.FloatField(
                                                null=True,
                                                blank=True)
    custo_disponibilidade_simulado = models.FloatField(
                                                null=True,
                                                blank=True)
    consumo_mes = models.FloatField(
                                      null=True,
                                      blank=True)
    economia_valor= models.FloatField(
                                      null=True,
                                      blank=True)
    economia_percentual=models.FloatField(
                                      null=True,
                                      blank=True)
    endereco = models.CharField (max_length=100, null=False, blank=True)
    energia_da_concessionaria = models.FloatField(
                                                    null=True,
                                                    blank=True)
    franquia = models.FloatField(
                                   null=True,
                                   blank=True)
    iluminacaoPublica = models.FloatField(
                                            null=True,
                                            blank=True)
    injetada = models.FloatField(
                                   null=True,
                                   blank=True)
    instalacao = models.IntegerField (null=True, blank=True)
    porte = models.CharField(max_length=15, null=True, blank=True)
    referencia = models.CharField (max_length=8, null=True, blank=True)
    tarifa = models.FloatField(
                                 null=True,
                                 blank=True)
    tarifaInjetada = models.FloatField(
                                         null=True,
                                         blank=True)
    totalSimulado = models.FloatField(
                                        null=True,
                                        blank=True)
    totalPagar = models.FloatField(
                                     null=True,
                                     blank=True)
    valorConsumoSimulado = models.FloatField(
                                               null=True,
                                               blank=True)
    valorInjetado = models.FloatField(
                                        null=True,
                                        blank=True)
    vencimento = models.CharField (max_length=12, null=True, blank=True)
    usuario = models.CharField(max_length=40, null=True, blank=True)
    cpf_cliente = models.ForeignKey(Cliente, models.SET_NULL,
        blank=True,
        null=True)

    def carregarConta(self, *args, **kwargs):
        '''
        Carrega uma conta de energia no objeto, extraindo do PDF os valores e armazenando-os nos atributos.

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
        extrairInstalacao: função
            parâmetro: string que contém a conta de energia
            saída: Integer contendo o número da instalação
        extrairReferencia: função
            parâmetro: string que contém a conta de energia
            saída: string contendo o mês e o ano da fatura MMM/AAAA (ex: ABR/2022)
        extrairEnergiaInjetada: função
            parâmetro: string que contém a conta de energia
            saída: float com a quantidade de energia injetada pelo gerador
        extrairCustoDisponibilidade: função
            parâmetro: string que contém a conta de energia
            saída: float contendo o custo de disponibilidade
        extrairVencimento: função
            parâmetro: string que contém a conta de energia
            saída: string contendo o mês e o ano da fatura DD/MM/AAAA
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
        instalacao
        referencia
        vencimento
        tarifa
        ----------

        '''
        pdf2txt = kwargs.get('pdf2txt', False)
        extrairPorte = kwargs.get('extrairPorte', False)
        extrairHistoricoConsumo = kwargs.get('extrairHistoricoConsumo', False)
        extrairNumeroInstalacao = kwargs.get('extrairNumeroInstalacao', False)
        extrairEnergiaInjetada = kwargs.get('extrairEnergiaInjetada', False)
        extrairReferencia = kwargs.get('extrairReferencia', False)
        extrairVencimento = kwargs.get('extrairVencimento', False)
        extrairCustoDisponibilidade = kwargs.get('extrairCustoDisponibilidade',
                                                 False)
        obterIluminacaoPublica = kwargs.get('obterIluminacaoPublica', False)
        
        if ((kwargs.get('conta_pdf') == None) and (self.conta_pdf==None)):
            print('Necessário informar o parâmetro "conta" ou preencher o atributo conta_pdf')
            return None

        self.conta_pdf = kwargs.get('conta_pdf', self.conta_pdf)
        self.desconto = kwargs.get('desconto', self.desconto)
        self.bonus = kwargs.get('bonus', self.bonus)
        
        conta_txt = pdf2txt(self.conta_pdf.path, 0)
        #print (conta_txt)
        self.porte = extrairPorte(conta_txt)

        self.injetada = extrairEnergiaInjetada(conta_txt)
        self.instalacao = extrairNumeroInstalacao(conta_txt)
        self.custo_disponibilidade = extrairCustoDisponibilidade(conta_txt)[0]
        self.custo_disponibilidade_simulado = extrairCustoDisponibilidade(conta_txt)[0]
        self.energia_da_concessionaria = extrairCustoDisponibilidade(
            conta_txt)[1]
        self.referencia= extrairReferencia(conta_txt)
        self.tarifa = extrairCustoDisponibilidade(conta_txt)[2]
        self.vencimento = extrairVencimento(conta_txt)
        self.iluminacaoPublica = obterIluminacaoPublica(conta_txt)
        consumos_mensais = extrairHistoricoConsumo(conta_txt)
        self.consumo_mes = consumos_mensais[0]

        self.tarifa = self.custo_disponibilidade / franquiaOficial[
            self.porte] if math.isnan(self.tarifa) else self.tarifa

        self.calcularFaturaSemEnergiaFotovoltaica()
        self.calcularFaturaComEnergiaFotovoltaica()
        self.calculaEconomia()

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
        economia_percentual
        economia_valor
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

        #Valor que o cliente deve repassar ao fornecedor de energia, considerando que o fornecedor
        #é responsável por pagar a fatura da concessionária
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

        
        if self.consumo_mes < franquiaOficial[
                self.
                porte]:
            self.valorConsumoSimulado = 0
        else:
            self.valorConsumoSimulado = float(self.consumo_mes) * self.tarifa
            self.custo_disponibilidade_simulado=0
 

        '''
        self.valorConsumoSimulado = franquiaOficial[
            self.porte] if self.valorConsumoSimulado < franquiaOficial[
                self.
                porte] else self.valorConsumoSimulado  #Caso o consumo seja menor que a franquia, colocar a franquia como consumo simulado
        '''
        self.totalSimulado = self.valorConsumoSimulado + self.custo_disponibilidade_simulado+ self.iluminacaoPublica
        
    def calculaEconomia(self, *args, **kwargs):
        '''
        Calcula propriedades relacionadas com a economia que o cliente teve ao contratar
        a energia fotovoltaica do gerador.

        ----------
        Parâmetro: nenhum
        ----------
        Saída: nenhuma
        ----------
        Atributos atualizados pelo método:
        economia_percentual
        economia_valor
        ----------

        '''

        self.economia_valor=self.totalSimulado-self.totalPagar
        self.economia_percentual=100*self.economia_valor/self.totalSimulado

    def imprimir_pdf(self):
        print (self.conta_pdf)
        # Creating Canvas
        c = canvas.Canvas("invoice.pdf",pagesize=pagesizes.A4,bottomup=0)
        # Logo Section
        # Setting th origin to (10,40)
        c.translate(30,80)
        # Inverting the scale for getting mirror Image of logo
        c.scale(1,-1)
        # Inserting Logo into the Canvas at required position
        c.drawImage("logo.jpg",0,0,width=50,height=30)
        # Title Section
        # Again Inverting Scale For strings insertion
        c.scale(1,-1)
        # Again Setting the origin back to (0,0) of top-left
        c.translate(-10,-40)
        # Setting the font for Name title of company
        c.setFont("Helvetica-Bold",20)
        # Inserting the name of the company
        c.drawCentredString(165,20,"CW Gestão Energia")
        # For under lining the title
        c.line(70,22,260,22)
        # Changing the font size for Specifying Address
        c.setFont("Helvetica-Bold",10)
        c.drawCentredString(165,35,"charles.wilis@gmail.com")
        # Changing the font size for Specifying GST Number of firm
        c.setFont("Helvetica-Bold",8)
        c.drawCentredString(165,45,"31 99926-8659")
        # Line Seprating the page header from the body
        c.line(5,58,555,58)
        # Document Information
        # Changing the font for Document title
        c.setFont("Courier-Bold",9.5)
        c.drawCentredString(252,68,"Faturamento de Energia Elétrica Injetada")
        # This Block Consist of Costumer Details
        c.roundRect(15,85,525,60,10,stroke=1,fill=0)
        c.setFont("Times-Bold",10)
        c.drawRightString(100,100,"Mês da referencia :")
        c.drawRightString(154,100,self.referencia)
        c.drawRightString(420,100,"Instalação :")
        c.drawRightString(475,100,str(self.instalacao))
        c.drawRightString(100,113,"Vencimento :")
        c.drawRightString(150,113,self.vencimento)
        c.drawRightString(100,126,"Cliente :")
        c.drawRightString(250,126,"Estovadão") 
        c.drawRightString(100,139,"Endereço :")
        c.drawRightString(280,139,self.endereco)
        c.drawRightString(480,139,"Desconto negociado no kwh: "+ str(self.desconto) + "%")
        c.roundRect(15,150,260,220,10,stroke=1,fill=0)
        c.setFont("Courier-Bold",11)
        c.drawCentredString(150,160,"Simulação SEM energia fotovoltaica")
        c.roundRect(280,150,260,220,10,stroke=1,fill=0)
        c.setFont("Times-Bold",10)
        c.drawRightString(80,180,"Consumo:")
        c.drawRightString(130,180, "{:.0f} KWh".format(self.consumo_mes))
        c.drawRightString(190,180,"x "+"R$ {:.2f}".format(self.tarifa))
        c.drawRightString(250,180,"R$ {:.2f}".format(self.valorConsumoSimulado))
        c.drawRightString(123,195,"Iluminação Pública:")
        c.drawRightString(250,195,"R$ "+str(self.iluminacaoPublica))
        c.drawRightString(145,210,"Custo de disponibilidade:")
        c.drawRightString(250,210,"R$ "+str(self.custo_disponibilidade_simulado))
        c.drawRightString(115,300,"Total da Conta:")
        c.drawRightString(250,300,"R$ {:.2f}".format(self.totalSimulado))


        c.setFont("Times-Bold",40)
        red50transparent = Color( 0, 0, 0, alpha=0.3)
        c.setFillColor(red50transparent)
        c.rotate(45)
        c.drawRightString(400,100,"Simulação")
        c.rotate(-45)
        red50transparent = Color( 0, 0, 0, alpha=1)
        c.setFillColor(red50transparent)


        c.setFont("Courier-Bold",11)
        c.drawCentredString(400,160,"Fatura COM energia fotovoltaica")
        c.setFont("Times-Bold",10)
        c.drawRightString(345,180,"Energia solar")
        c.drawRightString(399,180,str(self.injetada) + " KWh")
        c.drawRightString(454,180,"x "+"R$ "+"{:.2f}".format(self.tarifaInjetada))
        c.drawRightString(520,180,"R$ "+"{:.2f}".format(self.valorInjetado))
        c.drawRightString(374,195,"Iluminação Pública:")
        c.drawRightString(520,195,"R$ "+str(self.iluminacaoPublica))
        c.drawRightString(396,210,"Custo de disponibilidade:")
        c.drawRightString(440,210,"{:.0f}".format(self.consumo_mes-self.injetada) + " KWh")
        c.drawRightString(520,210,"R$ "+"{:.2f}".format(self.custo_disponibilidade))
        c.drawRightString(318,225,"Bônus:")
        c.drawRightString(520,225,"-R$ {:.2f}".format(self.bonus))
        c.drawRightString(335,300,"Economia:")
        c.drawRightString(393,300,"{:.2f}".format(self.economia_percentual) + "%")
        c.drawRightString(520,300,"R$ {:.2f}".format(self.economia_valor))
        c.drawRightString(350,320,"Total a pagar:")
        c.drawRightString(520,320,"R$ {:.2f}".format(self.totalPagar))
        c.roundRect(470, 305,60,20,3,stroke=1,fill=0)

        c.showPage()
        # Saving the PDF
        c.save()

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
        print ('Salvando e alterando o objeto Faturamento no save()')
        super().save(*args, **kwargs) #Tem que salvar antes, para gravar o arquivo pdf que foi modificado
        print ('salvei e saí do save()')
        '''print(self.conta_pdf)
        self.carregarConta(      
            pdf2txt=cemig.pdf2txt,
            extrairPorte=cemig.extrairPorte,
            extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig.extrairNumeroInstalacao,
            extrairReferencia=cemig.extrairReferencia,
            extrairVencimento=cemig.extrairVencimento
            )
        
        super().save(*args, **kwargs, force_update=True )
        '''

