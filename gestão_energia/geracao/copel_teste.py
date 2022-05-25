from numpy import histogram
import copel

pag1=copel.pdf2txt('tests/copel/Fatura_Com_Micro2.pdf',0)
print (pag1)

referencia=copel.extrairReferencia(pag1)
print (referencia)

vencimento=copel.extrairVencimento(pag1)
print (vencimento)

porte=copel.extrairPorte(pag1)
print (porte)

historico=copel.extrairHistoricoConsumo(pag1)
print (historico)

injetada=copel.extrairEnergiaInjetada(pag1)
print (injetada)

instalacao=copel.extrairNumeroInstalacao(pag1)
print (instalacao)

disponibilidade=copel.extrairCustoDisponibilidade(pag1)
print (disponibilidade)

ilimunacaoPublica=copel.obterIluminacaoPublica(pag1)
print (ilimunacaoPublica)

saldoResidual=copel.extrairSaldoResidual(pag1)
print (saldoResidual)