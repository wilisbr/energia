from django.test import TestCase
from geracao.cemig import extrairSaldoResidual
from geracao.models import Faturamento  #, pdf2txt
from django.conf import settings
import os
import sys
import inspect

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import cemig, cemig2, copel


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
        self.faturamentoUrbanoCopel = Faturamento()
        self.faturamentoRuralCopelSemInjetada = Faturamento()
        self.faturamentoRuralCopelComInjetada = Faturamento()
        self.faturamentoCemigBitencaNovo= Faturamento()
        self.faturamentoCemigEstovaNovo= Faturamento()
        self.faturamentoGoitacazesNova= Faturamento()
        #Carregando as contas 
        self.faturamentoGoitacazesNova.carregarConta(
            conta_pdf='geracao/tests/fatura_nova_gotacazes.pdf',
            pdf2txt=cemig2.pdf2txt,
            extrairPorte=cemig2.extrairPorte,
            extrairHistoricoConsumo=cemig2.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig2.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig2.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig2.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig2.extrairNumeroInstalacao,
            extrairReferencia=cemig2.extrairReferencia,
            extrairVencimento=cemig2.extrairVencimento,
            extrairSaldoResidual=cemig2.extrairSaldoResidual,
            desconto=20,
            bonus=30)

        self.faturamentoCemigBitencaNovo.carregarConta(
            conta_pdf='geracao/tests/fatura_nova_bitenca.pdf',
            pdf2txt=cemig2.pdf2txt,
            extrairPorte=cemig2.extrairPorte,
            extrairHistoricoConsumo=cemig2.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig2.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig2.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig2.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig2.extrairNumeroInstalacao,
            extrairReferencia=cemig2.extrairReferencia,
            extrairVencimento=cemig2.extrairVencimento,
            extrairSaldoResidual=cemig2.extrairSaldoResidual,
            desconto=20,
            bonus=30)
        self.faturamentoCemigEstovaNovo.carregarConta(
            conta_pdf='geracao/tests/FaturaCEMIG_11022023.pdf',
            pdf2txt=cemig2.pdf2txt,
            extrairPorte=cemig2.extrairPorte,
            extrairHistoricoConsumo=cemig2.extrairHistoricoConsumo,
            extrairEnergiaInjetada=cemig2.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=cemig2.extrairCustoDisponibilidade,
            obterIluminacaoPublica=cemig2.obterIluminacaoPublica,
            extrairNumeroInstalacao=cemig2.extrairNumeroInstalacao,
            extrairReferencia=cemig2.extrairReferencia,
            extrairVencimento=cemig2.extrairVencimento,
            extrairSaldoResidual=cemig2.extrairSaldoResidual,
            desconto=20,
            bonus=30)

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
            extrairSaldoResidual=copel.extrairSaldoResidual,
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
            extrairSaldoResidual=copel.extrairSaldoResidual,
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
            extrairSaldoResidual=copel.extrairSaldoResidual,
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
            extrairSaldoResidual=copel.extrairSaldoResidual,
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
            extrairSaldoResidual=copel.extrairSaldoResidual,
            desconto=20,
            bonus=0)
        self.faturamentoUrbanoCopel.carregarConta(
            conta_pdf='geracao/tests/copel/PrimeiraVia.pdf',
            pdf2txt=copel.pdf2txt,
            extrairPorte=copel.extrairPorte,
            extrairHistoricoConsumo=copel.extrairHistoricoConsumo,
            extrairEnergiaInjetada=copel.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=copel.extrairCustoDisponibilidade,
            obterIluminacaoPublica=copel.obterIluminacaoPublica,
            extrairNumeroInstalacao=copel.extrairNumeroInstalacao,
            extrairReferencia=copel.extrairReferencia,
            extrairVencimento=copel.extrairVencimento,
            extrairSaldoResidual=copel.extrairSaldoResidual,
            desconto=20,
            bonus=0
        )
        self.faturamentoRuralCopelSemInjetada.carregarConta(
            conta_pdf='geracao/tests/copel/Fatura_Com_Micro.pdf',
            pdf2txt=copel.pdf2txt,
            extrairPorte=copel.extrairPorte,
            extrairHistoricoConsumo=copel.extrairHistoricoConsumo,
            extrairEnergiaInjetada=copel.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=copel.extrairCustoDisponibilidade,
            obterIluminacaoPublica=copel.obterIluminacaoPublica,
            extrairNumeroInstalacao=copel.extrairNumeroInstalacao,
            extrairReferencia=copel.extrairReferencia,
            extrairVencimento=copel.extrairVencimento,
            extrairSaldoResidual=copel.extrairSaldoResidual,
            desconto=20,
            bonus=0
        )
        self.faturamentoRuralCopelComInjetada.carregarConta(
            conta_pdf='geracao/tests/copel/Fatura_Com_Micro2.pdf',
            pdf2txt=copel.pdf2txt,
            extrairPorte=copel.extrairPorte,
            extrairHistoricoConsumo=copel.extrairHistoricoConsumo,
            extrairEnergiaInjetada=copel.extrairEnergiaInjetada,
            extrairCustoDisponibilidade=copel.extrairCustoDisponibilidade,
            obterIluminacaoPublica=copel.obterIluminacaoPublica,
            extrairNumeroInstalacao=copel.extrairNumeroInstalacao,
            extrairReferencia=copel.extrairReferencia,
            extrairVencimento=copel.extrairVencimento,
            extrairSaldoResidual=copel.extrairSaldoResidual,
            desconto=20,
            bonus=0
        )

        
        #print("setUp: Run once for every test method to setup clean data.")
        pass


    def test_saldo_residual(self):
        self.assertEqual(self.faturamentoGoitacazesNova.acerto,43.59)

    def test_extrairPorte(self):
        #print("Testando método extrairPorte()")
        self.assertEqual(self.faturamentoGoitacazesAbril.porte, 'Monofásico')
        self.assertEqual(self.faturamentoCharlesAbril.porte, 'Bifásico')
        self.assertEqual(self.faturamentoRJAbril.porte, 'Trifásico')
        self.assertEqual(self.faturamentoEstovadaoAbril.porte, 'Trifásico')
        self.assertEqual(self.faturamentoRosi.porte, 'Bifásico')
        self.assertEqual(self.faturamentoUrbanoCopel.porte, 'Trifásico')
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.porte, 'Trifásico')
        self.assertEqual(self.faturamentoRuralCopelComInjetada.porte, 'Trifásico')
        self.assertEqual(self.faturamentoCemigBitencaNovo.porte, 'Bifásico')

    def test_extrairHistoricoConsumo(self):
        #print("Testando método extrairHistoricoConsumo()")
        self.assertEqual(self.faturamentoGoitacazesAbril.consumo_mes, 411)
        self.assertEqual(self.faturamentoCharlesAbril.consumo_mes, 304)
        self.assertEqual(self.faturamentoRJAbril.consumo_mes, 692)
        self.assertEqual(self.faturamentoEstovadaoAbril.consumo_mes, 238)
        self.assertEqual(self.faturamentoRosi.consumo_mes, 600)
        self.assertEqual(self.faturamentoUrbanoCopel.consumo_mes, 939)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.consumo_mes, 0)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.consumo_mes, 809)
        self.assertEqual(self.faturamentoCemigBitencaNovo.consumo_mes, 1136)

    def test_extrairEnergiaInjetada(self):
        #print("Testando método extrairEnergiaInjetada()")
        self.assertEqual(self.faturamentoGoitacazesAbril.injetada, 411)
        self.assertEqual(self.faturamentoCharlesAbril.injetada, 284)
        self.assertEqual(self.faturamentoRJAbril.injetada, 692)
        self.assertEqual(self.faturamentoEstovadaoAbril.injetada, 138)
        self.assertEqual(self.faturamentoRosi.injetada, 240)
        self.assertEqual(self.faturamentoUrbanoCopel.injetada, 839)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.injetada, 0)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.injetada, 709)
        self.assertEqual(self.faturamentoCemigBitencaNovo.injetada, 1086)

    def test_custo_disponibilidade(self):
        #print("Testando método custo_disponibilidade()")
        self.assertEqual(self.faturamentoGoitacazesAbril.custo_disponibilidade,
                         31.43)
        self.assertEqual(self.faturamentoCharlesAbril.custo_disponibilidade,
                         56.14)
        self.assertEqual(self.faturamentoRJAbril.custo_disponibilidade, 104.80)
        self.assertEqual(self.faturamentoEstovadaoAbril.custo_disponibilidade,
                         112.28)
        self.assertEqual(self.faturamentoRosi.custo_disponibilidade, 404.24)
        self.assertEqual(self.faturamentoUrbanoCopel.custo_disponibilidade, 104.25)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.custo_disponibilidade, 67.38)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.custo_disponibilidade, 60.95)
        self.assertEqual(self.faturamentoCemigBitencaNovo.custo_disponibilidade, 37.41)

    def test_obterIluminacaoPublica(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.iluminacaoPublica,
                         42.07)
        self.assertEqual(self.faturamentoCharlesAbril.iluminacaoPublica, 42.07)
        self.assertEqual(self.faturamentoRJAbril.iluminacaoPublica, 52.57)
        self.assertEqual(self.faturamentoEstovadaoAbril.iluminacaoPublica,
                         31.56)
        self.assertEqual(self.faturamentoRosi.iluminacaoPublica, 52.57)
        self.assertEqual(self.faturamentoUrbanoCopel.iluminacaoPublica, 41.78)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.iluminacaoPublica, 0)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.iluminacaoPublica, 0)
        self.assertEqual(self.faturamentoCemigBitencaNovo.iluminacaoPublica, 35.27)

    def test_franquia(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.franquia, 0)
        self.assertEqual(self.faturamentoCharlesAbril.franquia, 20)
        self.assertEqual(self.faturamentoRJAbril.franquia, 0)
        self.assertEqual(self.faturamentoEstovadaoAbril.franquia, 100)
        self.assertEqual(self.faturamentoRosi.franquia, 360)
        self.assertEqual(self.faturamentoUrbanoCopel.franquia, 100)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.franquia, 0)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.franquia, 100)
        self.assertEqual(self.faturamentoCemigBitencaNovo.franquia, 50)

    def test_totalPagar(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.totalPagar, 387.97)
        self.assertEqual(self.faturamentoCharlesAbril.totalPagar, 333.31)
        self.assertEqual(self.faturamentoRJAbril.totalPagar, 687.54)
        self.assertEqual(self.faturamentoEstovadaoAbril.totalPagar,
                         267.83)
        self.assertEqual(self.faturamentoRosi.totalPagar, 672.1700000000001)
        self.assertEqual(self.faturamentoUrbanoCopel.totalPagar, 845.76)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.totalPagar, 67.38)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.totalPagar, 345.71)
        self.assertEqual(self.faturamentoCemigBitencaNovo.totalPagar, 693.0699999999999)

    def test_valorConsumoSimulado(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.valorConsumoSimulado,
                         430.59)
        self.assertEqual(self.faturamentoCharlesAbril.valorConsumoSimulado,
                         341.33)
        self.assertEqual(self.faturamentoRJAbril.valorConsumoSimulado, 725.22)
        self.assertEqual(self.faturamentoEstovadaoAbril.valorConsumoSimulado,
                         267.29)
        self.assertEqual(self.faturamentoRosi.valorConsumoSimulado, 673.01)
        self.assertEqual(self.faturamentoUrbanoCopel.valorConsumoSimulado, 978.91)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.valorConsumoSimulado, 0)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.valorConsumoSimulado, 493.09)
        self.assertEqual(self.faturamentoCemigBitencaNovo.valorConsumoSimulado, 850.41)

    def test_totalSimulado(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.totalSimulado,
                         472.66)
        self.assertEqual(self.faturamentoCharlesAbril.totalSimulado, 383.4)
        self.assertEqual(self.faturamentoRJAbril.totalSimulado,
                         777.79)
        self.assertEqual(self.faturamentoEstovadaoAbril.totalSimulado,
                         298.85)
        self.assertEqual(self.faturamentoRosi.totalSimulado, 725.58)
        self.assertEqual(self.faturamentoUrbanoCopel.totalSimulado, 1020.69)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.totalSimulado, 67.38)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.totalSimulado, 432.14)
        self.assertEqual(self.faturamentoCemigBitencaNovo.totalSimulado, 885.68)

    def test_instalacao(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.instalacao,
                         3004078633)
        self.assertEqual(self.faturamentoCharlesAbril.instalacao, 3012091635)
        self.assertEqual(self.faturamentoRJAbril.instalacao,
                         3004549294)
        self.assertEqual(self.faturamentoEstovadaoAbril.instalacao,
                         3010475009)
        self.assertEqual(self.faturamentoRosi.instalacao, 3002307732)
        self.assertEqual(self.faturamentoUrbanoCopel.instalacao, 96322217)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.instalacao, 106414518)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.instalacao, 106414518)
        self.assertEqual(self.faturamentoCemigBitencaNovo.instalacao, 3007557368)
    
    def test_extrairReferencia(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.referencia,
                         'MAR/2022')
        self.assertEqual(self.faturamentoCharlesAbril.referencia, 'MAR/2022')
        self.assertEqual(self.faturamentoRJAbril.referencia,
                         'MAR/2022')
        self.assertEqual(self.faturamentoEstovadaoAbril.referencia,
                         'MAR/2022')
        self.assertEqual(self.faturamentoRosi.referencia, 'JAN/2022')
        self.assertEqual(self.faturamentoUrbanoCopel.referencia, 'ABR/2022')
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.referencia, 'MAR/2022')
        self.assertEqual(self.faturamentoRuralCopelComInjetada.referencia, 'ABR/2022')
        self.assertEqual(self.faturamentoCemigBitencaNovo.referencia, 'JAN/2023')

    def test_extrairVencimento(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.vencimento,
                         '11/04/2022')
        self.assertEqual(self.faturamentoCharlesAbril.vencimento, '11/04/2022')
        self.assertEqual(self.faturamentoRJAbril.vencimento,
                         '11/04/2022')
        self.assertEqual(self.faturamentoEstovadaoAbril.vencimento,
                         '11/04/2022')
        self.assertEqual(self.faturamentoRosi.vencimento, '11/02/2022')
        self.assertEqual(self.faturamentoUrbanoCopel.vencimento, '23/04/2022')
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.vencimento, '20/04/2022')
        self.assertEqual(self.faturamentoRuralCopelComInjetada.vencimento, '20/05/2022')
        self.assertEqual(self.faturamentoCemigBitencaNovo.vencimento, '02/02/2023')

    def test_calculaEconomia(self):
        self.assertEqual(self.faturamentoGoitacazesAbril.economia_percentual,
                         17.92)
        self.assertEqual(self.faturamentoCharlesAbril.economia_percentual, 13.06)
        self.assertEqual(self.faturamentoRJAbril.economia_percentual,
                         11.60)
        self.assertEqual(self.faturamentoEstovadaoAbril.economia_percentual,
                         10.38)
        self.assertEqual(self.faturamentoRosi.economia_percentual, 7.36)
        self.assertEqual(self.faturamentoUrbanoCopel.economia_percentual, 17.14)
        self.assertEqual(self.faturamentoRuralCopelSemInjetada.economia_percentual, 0)
        self.assertEqual(self.faturamentoRuralCopelComInjetada.economia_percentual, 17.53)
        self.assertEqual(self.faturamentoCemigBitencaNovo.economia_percentual, 21.75)

