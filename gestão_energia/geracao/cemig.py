import PyPDF2
import re
import numpy as np

#desconto = 0.2
#bonus = 30
franquiaOficial = {'Trifásico': 100, 'Bifásico': 50, 'Monofásico': 30}


def extrairExpressaoRegular(expr: str, texto: str) -> []:
    '''
    Método extrai, do texto, as ocorrências da expressão regular informada.

    parâmetros: expr: str; texto: str.

    saída: str[] contendo as ocorrênicas encontradas
    '''
    p = re.compile(expr)
    ocorrencias = p.findall(texto)
    #print(ocorrencias)
    #Convertendo para float as ocorrências numéricas
    for indice, ocorrencia in enumerate(ocorrencias):

        try:
            ocorrencias[indice] = float(ocorrencia.replace(',', '.'))
            #print("converti o valor " + str(ocorrencia) + " para float")
        except ValueError:
            #print(ocorrencia + " não é float")
            pass

    #retorna todas as ocorrências
    return ocorrencias if ocorrencias else ["none"]


def pdf2txt(arquivo: str, pagina: int) -> str:
    '''
    Extraí uma página do arquivo pdf e converte em txt.

    -----------
    Parâmetros: 
    arquivo:str : contém o nome do arquivo pdf, com a extensão. 
    pagina:int : número da página a ser extraída, iniciando no 0.
    -----------

    Saída:
    -----------
    str contendo a página excolhida
    -----------

    '''
    # Abrindo o arquivo pdf com a conta
    file = open(arquivo, 'rb')

    # Abrindo o leitor de PDF
    fileReader = PyPDF2.PdfFileReader(file)

    #Extraindo o texto, primeira página
    pag1 = fileReader.getPage(pagina).extractText()
    return (pag1)


def extrairPorte(pag1: str) -> str:
    '''
    Retorna o porte da conta

    ----------
    Parâmetro:
    str conténdo o texto com a conta de luz
    ----------

    Saída:
    ----------
    str contendo uma das saídas possíveis:
    'Monofásico'
    'Bifásico'
    'Trifásico'
    ----------

    '''
    p = re.compile("[a-zA-Z]*fásico")
    porte = p.findall(pag1)
    porte = porte[0] if porte else "indeterminado"
    return (porte)


def extrairHistoricoConsumo(pag1: str) -> []:
    '''
    Retorna o porte da conta

    ----------
    Parâmetro:
    str conténdo o texto com a conta de luz
    ----------

    Saída:
    ----------
    array contendo strings. Cada string é uma frase do tipo 'mes consumo'. Ex: 'janeiro 330':
    ----------

    '''
    consumos_mensais = extrairExpressaoRegular(r'[A-Z]{3}\/[0-9]{2}\s+\d+',
                                               pag1)
    consumos_mensais = [
        extrairExpressaoRegular(r'\d+$', x)[0] for x in consumos_mensais
    ]
    return (consumos_mensais)


def extrairEnergiaInjetada(pag1: str) -> float:
    '''
    Retorna a quantidade de energia fotovoltaica que foi injetada

    ----------
    Parâmetro:
    str conténdo o texto com a conta de luz
    ----------

    Saída:
    ----------
    float contendo a quantidade injetada
    ----------

    '''
    injetada = extrairExpressaoRegular(r'Energia injetada\D+\d+', pag1)[0]
    injetada = extrairExpressaoRegular(r'\d+', injetada)[0]
    return (injetada)


def extrairNumeroInstalacao(pag1: str) -> int:
    '''
    Retorna o número da instalação daquela fatura
    ----------
    Parâmetro:
    str conténdo o texto com a conta de luz
    ----------

    Saída:
    ----------
    int contendo o número da instalação
    ----------
    '''

    frase_contendo_numeros_instalacao_e_cliente = extrairExpressaoRegular(
        r'INSTALAÇÃO[0-9]+Referente', pag1)[0]
    numero_instalacao = int(frase_contendo_numeros_instalacao_e_cliente[20:29])
    return numero_instalacao

    

def extrairCustoDisponibilidade(pag1: str) -> float:
    '''
    Retorna o custo de indisponibildiade cobrado na fatura.
    Esse custo de disponibilidade pode gerar ou não créditos na fatura.
    Quando o período de leitura é menor que 30 dias, a Cemig não gera créditos.

    ----------
    Parâmetro:
    str conténdo o texto com a conta de luz
    ----------

    Saída:
    ----------
    tupla com três floats contendo :
    (valor_energia_concessionaria, quantidade_kwh_concessionaria, tarifa_energia_concessionaria)
    ----------

    '''
    #Quando não são gerados créditos:
    custo_disponibilidade = extrairExpressaoRegular(
        r'Custo de Disponibilidade\s*[0-9]+,[0-9]+', pag1)[0]
    valor_energia_concessionaria = extrairExpressaoRegular(
        '[0-9]+,[0-9]+', custo_disponibilidade)[0]
    quantidade_kwh_concessionaria = 0  #nao houve creditos
    tarifa_energia_concessionaria = np.NaN

    #Quando SÃO gerados créditos relacionados ao custo de disponibilidade ou ao consumo que nao foi suprido pela energia injetada
    if (custo_disponibilidade == 'none'):

        fornecimento_concessionaria = extrairExpressaoRegular(
            r'Energia Elétrica kWh\s+\d+\s+\d+,\d+\s+\d+,\d+', pag1)[0]
        valor_energia_concessionaria = extrairExpressaoRegular(
            '[0-9]+,[0-9]+', fornecimento_concessionaria)[1]
        tarifa_energia_concessionaria = extrairExpressaoRegular(
            '[0-9]+,[0-9]+', fornecimento_concessionaria)[0]
        quantidade_kwh_concessionaria = extrairExpressaoRegular(
            '[0-9]+', fornecimento_concessionaria)[0]
    return ((valor_energia_concessionaria, quantidade_kwh_concessionaria,
             tarifa_energia_concessionaria))


def obterIluminacaoPublica(pag1: str) -> float:
    '''
    Retorna a tarifa de iluminação pública cobrada na fatura.

    ----------
    Parâmetro:
    str conténdo o texto com a conta de luz
    ----------

    Saída:
    ----------
    float contendo o valor cobrado pela iluminação pública
    ----------

    '''
    iluminacaoPublica = extrairExpressaoRegular(r'Ilum Publica\D+\d+,\d+',
                                                pag1)[0]
    iluminacaoPublica = extrairExpressaoRegular(r'\d+,\d+',
                                                iluminacaoPublica)[0]
    return (iluminacaoPublica)


def gerarContaComFotovotaica(pdf_conta: str, desconto=0.2, bonus=0) -> float:
    '''
    Gera a conta com a energia fotovoltaica, discriminando cada valor.

    ----------
    Parâmetro:
    pdf_conta: Str com o nome do arquivo pdf da conta da Cemig
    desconto: float com o valor do desconto concedido na tarifa, em relação ao preço da CEMIG
    bonus: float com o valor que será creditado na conta, 

    ----------

    Saída:
    ----------
    float contendo o valor total da conta gerada
    Todo: retornar um objeto com todos os parâmetros da conta
    ----------

    '''
    pag1 = pdf2txt(pdf_conta, 0)
    porte = extrairPorte(pag1)
    consumos_mensais = extrairHistoricoConsumo(pag1)
    consumo_mes = consumos_mensais[0]
    injetada = extrairEnergiaInjetada(pag1)
    franquiaCemig = consumo_mes - injetada
    custo_disponibilidade = extrairCustoDisponibilidade(pag1)
    tarifaCemig = custo_disponibilidade / franquiaOficial[porte]

    #Tarifa cobrada do cliente, com o desconto definido
    tarifaInjetada = (1 - desconto) * tarifaCemig

    #Valor que será cobrado do cliente pela energia injetada
    valorInjetado = tarifaInjetada * injetada

    iluminacaoPublica = obterIluminacaoPublica(pag1)

    totalPagar = iluminacaoPublica + custo_disponibilidade + valorInjetado - bonus

    print('---------------Conta atual (com desconto)-------------')
    print('Tarifa da energia injetada: ' + str(tarifaInjetada))
    print('Energia injetada (kw/h): ' + str(injetada) + '   R$: ' +
          str(valorInjetado))
    print('Iluminação pública: ' + str(iluminacaoPublica))
    print('Franquia Cemig: ' + str(franquiaCemig))
    print('Custo de disponibilidade: ' + str(custo_disponibilidade))
    print('Bônus cortesia: -' + str(bonus))
    print('Total a pagar: R$ ' + str(totalPagar))
    print('------------------------------------------------------\n\n')

    return (totalPagar)


def simularContaSemFotovotaica(pdf_conta: str) -> float:
    '''
    Simula a conta SEM a energia fotovoltaica, discriminando cada valor.

    ----------
    Parâmetro:
    Str com o nome do arquivo pdf da conta da Cemig
    ----------

    Saída:
    ----------
    float contendo o valor total da conta simulada
    Todo: retornar um objeto com todos os parâmetros da conta
    ----------

    '''
    pag1 = pdf2txt(pdf_conta, 0)
    porte = extrairPorte(pag1)
    consumos_mensais = extrairHistoricoConsumo(pag1)
    consumo_mes = consumos_mensais[0]
    custo_disponibilidade = extrairCustoDisponibilidade(pag1)
    tarifaCemig = custo_disponibilidade / franquiaOficial[porte]
    valorConsumoSimulado = float(consumo_mes) * tarifaCemig
    valorConsumoSimulado = franquiaOficial[
        porte] if valorConsumoSimulado < franquiaOficial[
            porte] else valorConsumoSimulado  #Caso o consumo seja menor que a franquia, colocar a franquia como consumo simulado

    iluminacaoPublica = obterIluminacaoPublica(pag1)

    totalSimulado = valorConsumoSimulado + iluminacaoPublica

    print('---------Simulação SEM energia fotovoltaica-----------')
    print('Tarifa CEMIG: ' + str(tarifaCemig))
    print('Consumo simulado: ' + str(valorConsumoSimulado))
    print('Iluminação pública: ' + str(iluminacaoPublica))
    print('Total da conta simulada: R$ ' + str(totalSimulado))
    print('------------------------------------------------------\n\n')

    return (totalSimulado)


'''
totalSimulado = simularContaSemFotovotaica('FaturaCEMIG_11042022_AP.pdf')
totalPagar = gerarContaComFotovotaica('FaturaCEMIG_11042022_AP.pdf', bonus=20)

economia = totalSimulado - totalPagar
economiaPercentual = 100 * economia / totalSimulado
print('Economia de R$ ' + str(economia) + ' = ' + str(economiaPercentual) +
      '%')
'''