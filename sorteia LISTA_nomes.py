import random

alunos = ['maria', 'jose', 'pedro', 'juca']
sorteados = []

for c in range(4):
    sorteados.append(random.choice(alunos))
    alunos.remove(sorteados[c])

print(sorteados)


