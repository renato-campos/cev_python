# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 58: melhore o jogo do exercício 028 onde o computador vai
# 'pensar' um número entre a e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

from random import randint
from time import sleep

computer = randint(0, 10)
user = None
count = 0
while computer != user:
    user = int(input('\nDigite um número entre 0 e 10: '))
    count += 1
    if user < computer:
        print('\nVocê errou, tente outro maior!')
    elif user > computer:
        print('\nVocê errou, tente outro menor!')

print(f'\nParabéns, você acertou em {count} tentativas!')
