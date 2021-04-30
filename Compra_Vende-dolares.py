from funcoes import *

resp = ''
print('Você deseja comprar ou vender dólares?')

while True:
    try:
        resp = input('Comprar[C] / Vender[V]: ').upper()
    except:
        print('Por favor digite um valor válido ')
    else:
        if resp in 'VC':
            break

if resp == 'C': # comprar
    while True:
        try:
            real = float(input('Digite a quantia em R$: '))
        except:
            print('Digite um valor inteiro')
        else:
            if type(real) == float:
                print(f'Com R$ {real} dá pra comprar {dolar_real(real):.2f} dólares!')
                break
else:
    while True:
        try:
            dolares = float(input('Digite quantos dólares deseja vender: '))
        except:
            print('Por favor digite um valor válido ')
        else:
            if type(dolares) == float:
                print(f'Com {dolares} dólares, darão R$ {dolar_real(dolares, dolar=True)}')
                break