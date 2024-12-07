import pytest

from .cemig import pdf2txt, extrairPorte, extrairHistoricoConsumo, extrairEnergiaInjetada, extrairCustoDisponibilidade, obterIluminacaoPublica

conta_goitacazes_abril = pdf2txt('noname.pdf', 0)
conta_charles_abril = pdf2txt('FaturaCEMIG_11042022_AP.pdf', 0)
conta_rj_abril = pdf2txt('FaturaCEMIG_11042022.pdf', 0)
conta_estovadao_abril = pdf2txt('556815429578.pdf', 0)


def test_extrairPorte():
    assert extrairPorte(conta_goitacazes_abril) == 'Monofásico'
    assert extrairPorte(conta_charles_abril) == 'Bifásico'
    assert extrairPorte(conta_rj_abril) == 'Trifásico'
    assert extrairPorte(conta_estovadao_abril) == 'Trifásico'


def test_extrairHistoricoConsumo():
    assert extrairHistoricoConsumo(conta_goitacazes_abril)[0] == 411
    assert extrairHistoricoConsumo(conta_charles_abril)[0] == 304
    assert extrairHistoricoConsumo(conta_rj_abril)[0] == 692
    assert extrairHistoricoConsumo(conta_estovadao_abril)[0] == 238


def test_extrairEnergiaInjetada():
    assert extrairEnergiaInjetada(conta_goitacazes_abril) == 411
    assert extrairEnergiaInjetada(conta_charles_abril) == 284
    assert extrairEnergiaInjetada(conta_rj_abril) == 692
    assert extrairEnergiaInjetada(conta_estovadao_abril) == 138


def test_extrairCustoDisponibilidade():
    assert extrairCustoDisponibilidade(conta_goitacazes_abril) == 31.43
    assert extrairCustoDisponibilidade(conta_charles_abril) == 56.14
    assert extrairCustoDisponibilidade(conta_rj_abril) == 104.80
    assert extrairCustoDisponibilidade(conta_estovadao_abril) == 112.28


def test_obterIluminacaoPublica():
    assert obterIluminacaoPublica(conta_goitacazes_abril) == 42.07
    assert obterIluminacaoPublica(conta_charles_abril) == 42.07
    assert obterIluminacaoPublica(conta_rj_abril) == 52.57
    assert obterIluminacaoPublica(conta_estovadao_abril) == 31.56