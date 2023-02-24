# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 18

# Exercício 88: faça um programa que ajude um jogador da mega sena a criar
# palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
from time import sleep

print(f'''{"-" * 40}
{"JOGOS DA MEGA SENA":^40}
{"-" * 40}''')
num_jogos = int(input('Número de jogos: '))
todos_jogos = []
jogo = []
for j in range(num_jogos):              # número de jogos a criar
    while len(jogo) < 6:                # garante 6 nº em cada jogo
        number = randint(0, 60)
        if number not in jogo:          # garante nº não repetido
            jogo.append(number)
    jogo.sort()
    if jogo not in todos_jogos:         # garante jogos não repetidos
        todos_jogos.append(jogo[:])
    jogo.clear()                        # zera o jogo para criação de um novo
todos_jogos.sort()
print(f'{"-=" * 3} SORTEANDO {num_jogos} JOGOS {"=-" * 3}')
for j in range(len(todos_jogos)):
    sleep(0.5)
    print(f'Jogo {j+1:>2}: {todos_jogos[j]}')
print('-=' * 4, '< BOA SORTE! >', '=-' * 4)
