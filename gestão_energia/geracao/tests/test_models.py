from django.test import TestCase
from geracao.models import Faturamento  #, pdf2txt
from django.conf import settings
import os
import sys
import inspect

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import cemig


# Create your tests here.
class TesteFaturamento(TestCase):

    @classmethod
    def setUpTestData(cls):
        print(
            "setUpTestData: Run once to set up non-modified data for all class methods."
        )

        pass

    def setUp(self):
        #Criando objetos para cada faturamento
        self.faturamentoGoitacazesAbril = Faturamento()
        self.faturamentoCharlesAbril = Faturamento()
        self.faturamentoRJAbril = Faturamento()
        self.faturamentoEstovadaoAbril = Faturamento()
        self.faturamentoRosi = Faturamento()

        #Carregando as contas
        self.faturamentoGoitacazesAbril.carregarConta(
            conta_pdf='geracao/tests/noname.pdf',
            pdf2txt=cemig.pdf2txt,
            extrairPorte=cemig.extrairPorte,
            extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig.extrairNumeroInstalacao,
            extrairReferencia=cemig.extrairReferencia,
            extrairVencimento=cemig.extrairVencimento,
            desconto=20,
            bonus=30)
        self.faturamentoCharlesAbril.carregarConta(
            conta_pdf='geracao/tests/FaturaCEMIG_11042022_AP.pdf',
            pdf2txt=cemig.pdf2txt,
            extrairPorte=cemig.extrairPorte,
            extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig.extrairNumeroInstalacao,
            extrairReferencia=cemig.extrairReferencia,
            extrairVencimento=cemig.extrairVencimento,
            desconto=20,
            bonus=20),
            
        self.faturamentoRJAbril.carregarConta(
            conta_pdf='geracao/tests/FaturaCEMIG_11042022.pdf',
            pdf2txt=cemig.pdf2txt,
            extrairPorte=cemig.extrairPorte,
            extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig.extrairNumeroInstalacao,
            extrairReferencia=cemig.extrairReferencia,
            extrairVencimento=cemig.extrairVencimento,
            desconto=20,
            bonus=50)
        self.faturamentoEstovadaoAbril.carregarConta(
            conta_pdf='geracao/tests/556815429578.pdf',
            pdf2txt=cemig.pdf2txt,
            extrairPorte=cemig.extrairPorte,
            extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig.extrairNumeroInstalacao,
            extrairReferencia=cemig.extrairReferencia,
            extrairVencimento=cemig.extrairVencimento,
            desconto=20,
            bonus=0)
        self.faturamentoRosi.carregarConta(
            conta_pdf='geracao/tests/876611782018.pdf',
            pdf2txt=cemig.pdf2txt,
            extrairPorte=cemig.extrairPorte,
            extrairHistoricoConsumo=cemig.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig.extrairNumeroInstalacao,
            extrairReferencia=cemig.extrairReferencia,
            extrairVencimento=cemig.extrairVencimento,
            desconto=20,
            bonus=0)
        #print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_extrairInstalacao(self):        
        self.assertEqual(self.faturamentoGoitacazesAbril.porte, 'Monofásico')
        self.assertEqual(self.faturamentoCharlesAbril.porte, 'Bifásico')
        self.assertEqual(self.faturamentoRJAbril.porte, 'Trifásico')
        self.assertEqual(self.faturamentoEstovadaoAbril.porte, 'Trifásico')
        self.assertEqual(self.faturamentoRosi.porte, 'Bifásico')

    def test_extrairPorte(self):
        print("Testando método extrairPorte()")
        self.assertEqual(self.faturamentoGoitacazesAbril.porte, 'Monofásico')
        self.assertEqual(self.faturamentoCharlesAbril.porte, 'Bifásico')
        self.assertEqual(self.faturamentoRJAbril.porte, 'Trifásico')
        self.assertEqual(self.faturamentoEstovadaoAbril.porte, 'Trifásico')
        self.assertEqual(self.faturamentoRosi.porte, 'Bifásico')

    def test_extrairHistoricoConsumo(self):
        print("Testando método extrairHistoricoConsumo()")
        self.assertEqual(self.faturamentoGoitacazesAbril.consumo_mes, 411)
        self.assertEqual(self.faturamentoCharlesAbril.consumo_mes, 304)
        self.assertEqual(self.faturamentoRJAbril.consumo_mes, 692)
        self.assertEqual(self.faturamentoEstovadaoAbril.consumo_mes, 238)
        self.assertEqual(self.faturamentoRosi.consumo_mes, 600)

    def test_extrairEnergiaInjetada(self):
        print("Testando método extrairEnergiaInjetada()")
        self.assertEqual(self.faturamentoGoitacazesAbril.injetada, 411)
        self.assertEqual(self.faturamentoCharlesAbril.injetada, 284)
        self.assertEqual(self.faturamentoRJAbril.injetada, 692)
        self.assertEqual(self.faturamentoEstovadaoAbril.injetada, 138)
        self.assertEqual(self.faturamentoRosi.injetada, 240)

    def test_custo_disponibilidade(self):
        print("Testando método custo_disponibilidade()")
        self.assertEqual(self.faturamentoGoitacazesAbril.custo_disponibilidade,
                         31.43)
        self.assertEqual(self.faturamentoCharlesAbril.custo_disponibilidade,
                         56.14)
        self.assertEqual(self.faturamentoRJAbril.custo_disponibilidade, 104.80)
        self.assertEqual(self.faturamentoEstovadaoAbril.custo_disponibilidade,
                         112.28)
        self.assertEqual(self.faturamentoRosi.custo_disponibilidade, 404.24)

    def test_obterIluminacaoPublica(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.iluminacaoPublica,
                         42.07)
        self.assertEqual(self.faturamentoCharlesAbril.iluminacaoPublica, 42.07)
        self.assertEqual(self.faturamentoRJAbril.iluminacaoPublica, 52.57)
        self.assertEqual(self.faturamentoEstovadaoAbril.iluminacaoPublica,
                         31.56)
        self.assertEqual(self.faturamentoRosi.iluminacaoPublica, 52.57)

    def test_franquia(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.franquia, 0)
        self.assertEqual(self.faturamentoCharlesAbril.franquia, 20)
        self.assertEqual(self.faturamentoRJAbril.franquia, 0)
        self.assertEqual(self.faturamentoEstovadaoAbril.franquia, 100)
        self.assertEqual(self.faturamentoRosi.franquia, 360)

    def test_totalPagar(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.totalPagar, 387.9728)
        self.assertEqual(self.faturamentoCharlesAbril.totalPagar, 333.31016)
        self.assertEqual(self.faturamentoRJAbril.totalPagar, 687.5428)
        self.assertEqual(self.faturamentoEstovadaoAbril.totalPagar,
                         267.827114576)
        self.assertEqual(self.faturamentoRosi.totalPagar, 672.17245632)

    def test_valorConsumoSimulado(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.valorConsumoSimulado,
                         430.591)
        self.assertEqual(self.faturamentoCharlesAbril.valorConsumoSimulado,
                         341.3312)
        self.assertEqual(self.faturamentoRJAbril.valorConsumoSimulado, 725.216)
        self.assertEqual(self.faturamentoEstovadaoAbril.valorConsumoSimulado,
                         267.29106222)
        self.assertEqual(self.faturamentoRosi.valorConsumoSimulado, 673.007676)

    def test_totalSimulado(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.totalSimulado,
                         472.661)
        self.assertEqual(self.faturamentoCharlesAbril.totalSimulado, 383.4012)
        self.assertEqual(self.faturamentoRJAbril.totalSimulado,
                         777.7860000000001)
        self.assertEqual(self.faturamentoEstovadaoAbril.totalSimulado,
                         298.85106222)
        self.assertEqual(self.faturamentoRosi.totalSimulado, 725.577676)

    def test_instalacao(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.instalacao,
                         3004078633)
        self.assertEqual(self.faturamentoCharlesAbril.instalacao, 3012091635)
        self.assertEqual(self.faturamentoRJAbril.instalacao,
                         3004549294)
        self.assertEqual(self.faturamentoEstovadaoAbril.instalacao,
                         3010475009)
        self.assertEqual(self.faturamentoRosi.instalacao, 3002307732)
    
    def test_extrairReferencia(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.referencia,
                         'MAR/2022')
        self.assertEqual(self.faturamentoCharlesAbril.referencia, 'MAR/2022')
        self.assertEqual(self.faturamentoRJAbril.referencia,
                         'MAR/2022')
        self.assertEqual(self.faturamentoEstovadaoAbril.referencia,
                         'MAR/2022')
        self.assertEqual(self.faturamentoRosi.referencia, 'JAN/2022')

    def test_extrairVencimento(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.vencimento,
                         '11/04/2022')
        self.assertEqual(self.faturamentoCharlesAbril.vencimento, '11/04/2022')
        self.assertEqual(self.faturamentoRJAbril.vencimento,
                         '11/04/2022')
        self.assertEqual(self.faturamentoEstovadaoAbril.vencimento,
                         '11/04/2022')
        self.assertEqual(self.faturamentoRosi.vencimento, '11/02/2022')

