def aumento(valor, porc):
    """
    :param valor: um inteiro
    :param porc: valor do percentual
    :return: valor com aumento percentual
    """
    aumento = valor + (valor / 100 * porc)
    return aumento

while True:
    try:
        valor = float(input('Digite um valor: '))
    except:
        print('Valor inválido!')
    else:
        print('-=' * 20)
        while True:
            try:
                aumentar = float(input('Digite o aumento: '))
            except:
                print('Valor inválido!')
            else:
                resultado = aumento(valor, aumentar)
                print(f'O aumento foi de: {resultado}')
                break
        break

print('Fim do programa')
