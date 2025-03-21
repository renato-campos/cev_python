# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 19

# Exercício 91: crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário. No final,
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior dado

from random import randint
from time import sleep
from operator import itemgetter

resultado = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

resultado2 = sorted(resultado.items(), key=itemgetter(1), reverse=True)
print('<<<< CLASSIFICAÇÃO >>>>')
for k, v in enumerate(resultado2):
    sleep(0.75)
    print(f"{k+1}º lugar -> {v[0]} com {v[1]}")
