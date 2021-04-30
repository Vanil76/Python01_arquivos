from funcoes import media

while True:
    try:
        num1 = float(input('digite o primeiro valor: '))
    except:
        print('Digite um valor inteiro válido')
    else:
        if type(num1) is float:
            break
while True:
    try:
        num2 = float(input('digite o segundo valor: '))
    except:
        print('Digite um valor inteiro válido')
    else:
        if type(num2) is float:
            break

media1 = media(num1, num2)

print(f'A média do aluno foi {media1}')