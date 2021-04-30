def leiaInteiro(ent):
    saida = False
    while not saida: #not saida = True
        try:
            a = int(input(ent))
            return a
        except ValueError:
                print('Erro: digite um número inteiro válido')

def leiaFloat(ent):
    while True:
        try:
            saida = float(input(ent))
            return saida
        except ValueError:
            print('Erro: digite um número inteiro válido')


inteiro = leiaInteiro('Digite um Inteiro: ')
flutuante = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {flutuante}')


