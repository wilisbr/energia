import PyPDF2
import pdfplumber
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


    file = pdfplumber.open(file)
    pag1 = file.pages[0].extract_text()

    return (pag1)

def extrairReferencia(pag1: str) -> str:
    '''
    Retorna o mês base da fatura

    ----------
    Parâmetro:
    str contendo o texto com a conta de luz
    ----------

    Saída:
    ----------
    str contendo MMM/AAAA (ex: ABR/2022)
    ----------
    '''
    texto_contendo_referencia=extrairExpressaoRegular(r'[A-zÀ-ú]+\/[\d]{4}', pag1)[0]
    referencia=texto_contendo_referencia[0:3]+'/'+texto_contendo_referencia[-4:]
    return (referencia.upper())

def extrairVencimento(pag1: str) -> str:
    '''
    Retorna a data de vencimento da fatura

    ----------
    Parâmetro:
    str contendo o texto com a conta de luz
    ----------

    Saída:
    ----------
    str contendo DD/MM/AAAA (ex: 11/04/2022)
    ----------
    '''
    vencimento=extrairExpressaoRegular(r'\d{2}\/\d{2}\/\d{4}', pag1)[0]
    return (vencimento)

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
    tradutor={
        'MONOFASICO':'Monofásico',
        'BIFASICO':'Bifásico',
        'TRIFASICO':'Trifásico'
    }
    p = re.compile("[A-Z]*FASICO")
    porte = p.findall(pag1)
    porte = porte[0] if porte else "indeterminado"
    return (tradutor[porte])


def extrairHistoricoConsumo(pag1: str) -> []:
    '''
    Retorna o histórico de consumo

    ----------
    Parâmetro:
    str conténdo o texto com a conta de luz
    ----------

    Saída:
    ----------
    array contendo strings. Cada string é uma frase do tipo 'mes consumo'. Ex: 'janeiro 330':
    ----------

    '''
    #Consumo do mês:
    texto_consumo_mes=extrairExpressaoRegular(r'\d+\skWh',pag1)[0]
    consumo_mes=extrairExpressaoRegular(r'\d+',texto_consumo_mes)

    #histórico de consumo anterior:
    consumos_mensais=extrairExpressaoRegular(r'\d{2}\/\d{4}\s\d+\s+\d',
    
                                               pag1)
    consumos_mensais = [extrairExpressaoRegular(r'\s\d+\s', x)[0] for x in consumos_mensais]
    
    #Unindo os dois:
    consumos_mensais=consumo_mes +consumos_mensais
    
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
    injetada = extrairExpressaoRegular(r'MINI GERACAO kWh\s\d+', pag1)[0]
    
    if injetada=='none':
        return 0
    
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
        r'[A-zÀ-ú]+\/[\d]{4}\s+\d+', pag1)[0]
    numero_instalacao = int (extrairExpressaoRegular(
        r'\s\d+', frase_contendo_numeros_instalacao_e_cliente)[0]) 
    #int(frase_contendo_numeros_instalacao_e_cliente[0:10])
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
    texto_energia_concessionaria_consumo=extrairExpressaoRegular(r'CONSUMO kWh\s\S+\s\S+\s\S+',pag1)[0]
    if (texto_energia_concessionaria_consumo=='none'):
        valor_consumo=0
        quantidade_consumo=0
    else:
        texto_energia_concessionaria_consumo=texto_energia_concessionaria_consumo.replace("CONSUMO kWh", "")
        texto_energia_concessionaria_consumo=texto_energia_concessionaria_consumo.split()
        valor_consumo=float(texto_energia_concessionaria_consumo[2].replace(',', '.'))
        quantidade_consumo=float(texto_energia_concessionaria_consumo[0])
    
    texto_uso_sistema=extrairExpressaoRegular(r'USO SISTEMA kWh\s\S+\s\S+\s\S+',pag1)[0]
    if (texto_uso_sistema=='none'):
        valor_uso_sistema=0
    else:
        texto_uso_sistema=texto_uso_sistema.replace("USO SISTEMA kWh", "")
        texto_uso_sistema=texto_uso_sistema.split()
        valor_uso_sistema=float(texto_uso_sistema[2].replace(',', '.'))
    
    #Custo de disponibilidade
    texto_disponibilidade=extrairExpressaoRegular(r'CUSTO DISP SISTEMA.*',pag1)[0]
    if (texto_disponibilidade!='none'):
        quantidade_disponibilidade=extrairExpressaoRegular(r'\d+',texto_disponibilidade)[0]
        valor_disponibilidade=extrairExpressaoRegular(r'\d+,\d+',texto_disponibilidade)[1]
    else:
        quantidade_disponibilidade=0
        valor_disponibilidade=0
    #

    texto_bandeira=extrairExpressaoRegular(r'ESCASSEZ HID kWh\s\S+',pag1)[0]
    texto_bandeira=texto_bandeira.replace('ESCASSEZ HID kWh ','')
    bandeira=0 if texto_bandeira == 'none' else float(texto_bandeira.replace(',', '.'))
    '''
    texto_subsidio_te=extrairExpressaoRegular(r'SUBSIDIO TARIFARIO TE\s\S+',pag1)[0]
    texto_subsidio_te=texto_subsidio_te.replace('SUBSIDIO TARIFARIO TE ','')
    subsidio_te=0 if texto_subsidio_te == 'none' else float(texto_subsidio_te.replace(',', '.'))

    texto_subsidio_uso=extrairExpressaoRegular(r'SUBSIDIO TARIFARIO TUSD\s\S+',pag1)[0]
    texto_subsidio_uso=texto_subsidio_uso.replace('SUBSIDIO TARIFARIO TUSD ','')
    subsidio_uso=0 if texto_subsidio_uso == 'none' else float(texto_subsidio_uso.replace(',', '.'))

    texto_subsidio=extrairExpressaoRegular(r'SUBSIDIO TARIFARIO\s\S+',pag1)[0]
    texto_subsidio=texto_subsidio.replace('SUBSIDIO TARIFARIO ','')
    subsidio=0 if texto_subsidio == 'none' else float(texto_subsidio.replace(',', '.'))
    '''
    subsidio=0
    textos_subsidio_tarifario=extrairExpressaoRegular(r'SUBSIDIO TARIFARIO.*',pag1)
    if (textos_subsidio_tarifario[0]!='none'):
        for texto_subsidio_tarifario in textos_subsidio_tarifario:
            subsidio+=extrairExpressaoRegular(r'-?\d+,\d+',texto_subsidio_tarifario)[0]

    valor_energia_concessionaria=valor_consumo+valor_uso_sistema+bandeira+subsidio+valor_disponibilidade
    quantidade_kwh_concessionaria=quantidade_consumo+quantidade_disponibilidade
    tarifa_energia_concessionaria=valor_energia_concessionaria/quantidade_kwh_concessionaria
    return (valor_energia_concessionaria, quantidade_kwh_concessionaria, tarifa_energia_concessionaria)


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
    iluminacaoPublica = extrairExpressaoRegular(r'ILUMIN PUBLICA MUNICIPIO \S*',
                                                pag1)[0]
    if (iluminacaoPublica!='none'):
        iluminacaoPublica = extrairExpressaoRegular(r'\d+,\d+',
                                                    iluminacaoPublica)[0]
        return (iluminacaoPublica)
    else:
        return 0

def extrairSaldoResidual(pag1: str) -> float:
    '''
    Retorna o saldo residual creditado à fatura das instalações rurais, pois é comum ocorrer leitura a maior,
    dado que alguma medições são feitas pela média.

    ----------
    Parâmetro:
    str conténdo o texto com a conta de luz
    ----------

    Saída:
    ----------
    float contendo o valor creditado na conta de luz pela iluminação pública.
    Se o valor for negativo, havia um valor devido que foi descontado nessa fatura.
    ----------

    '''
    saldo_residual=0
    textos_creditos_e_debitos = extrairExpressaoRegular(r'AJUSTE.*',
                                                pag1)
    if (textos_creditos_e_debitos[0]!='none'):
        for texto_creditos_e_debitos in textos_creditos_e_debitos:
            saldo_residual+=extrairExpressaoRegular(r'-?\d+,\d+',texto_creditos_e_debitos)[0]
    
    textos_creditos_e_debitos = extrairExpressaoRegular(r'SALDO A DEVOLVER.*',pag1)
    if (textos_creditos_e_debitos[0]!='none'):
        for texto_creditos_e_debitos in textos_creditos_e_debitos:
            saldo_residual+=extrairExpressaoRegular(r'-?\d+,\d+',texto_creditos_e_debitos)[0]
    return round(saldo_residual,2)

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
    custo_disponibilidade = round(extrairCustoDisponibilidade(pag1),2)
    tarifaCemig = custo_disponibilidade / franquiaOficial[porte]

    #Tarifa cobrada do cliente, com o desconto definido
    tarifaInjetada = (1 - desconto) * tarifaCemig

    #Valor que será cobrado do cliente pela energia injetada
    valorInjetado = round(tarifaInjetada * injetada,2)

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
    valorConsumoSimulado = round(float(consumo_mes) * tarifaCemig,2)
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