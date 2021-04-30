def somar(val1, val2):
    """
    :param val1: um inteiro
    :param val2: um inteiro
    :return: a soma de dois valores inteiros
    """
    res = val1 + val2
    return res


def desconto(valor, desc):
    """
    :param valor: um inteiro
    :param desc: o desconto que será dado
    :return: o desconto de um valor inteiro
    """
    res = valor - (valor / 100 * desc)
    return res


def aumento(valor, porc):
    """
    :param valor: um inteiro
    :param porc: valor do percentual
    :return: valor com aumento percentual
    """
    aumento = valor + (valor / 100 * porc)
    return aumento


def media(val1, val2):
    """
    :param val1: valor 1
    :param val2: valor 1
    :return: a soma dos valores de entrada por dois (para médias escolares)
    """
    media = (val1 + val2) / 2
    return media


def metro_mm(val):
    mm = val * 1000
    return mm


def metro_cent(val):
    cent = val * 100
    return cent


def multiplica(a, b):
    res = a * b
    return res


def dolar_real(valor_em_real, dolar=False):
    if dolar:  # SE dolar for True
        reais = valor_em_real * 5.59
        return reais
    else:  # SE dolar for False
        dolar = valor_em_real / 5.59
        return dolar


def leia_medida(Largura, altura):
    Largura = Largura
    altura = altura
    while True:
        try:
            Largura = float(input(f'Digite um valor para {Largura}: '))
        except:
            print('Por favor, digite um valor inteiro')
        else:
            if type(Largura) == float:
                break
    while True:
        try:
            altura = float(input(f'Digite um valor para {altura}: '))
        except:
            print('Por favor, digite um valor inteiro')
        else:
            if type(altura) == float:
                break

    return altura, Largura
