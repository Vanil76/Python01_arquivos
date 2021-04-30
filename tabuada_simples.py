from funcoes import *

print('-' * 30)
while True:
    try:
        numero = int(input('Digite um valor: '))
    except:
        print('Digite um valor válido')
    else:
        if type(numero) == int:
            break

for contador in range(1, 11):
    print(f'{numero} x {contador:>2} = {multiplica(numero, contador):>3}')
print('-' * 30)
