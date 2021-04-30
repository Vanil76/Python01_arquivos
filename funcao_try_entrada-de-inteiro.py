
def funcTry(msg):
    valor = None
    while True:
        try:
            valor = float(input(f'{msg}'))
        except:
            print('Valor inválido, tente novamente')
        else:
            if type(valor) == float:
                return valor

x = funcTry('Digite um número: ')
print(x)