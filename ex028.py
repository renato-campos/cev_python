# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 10

# Exercício 28: escreva um programa que faça o computador 'pensar'
# entre um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

secret = randint(0, 5)

print(f'{"Jogo da Adivinhação":=^30}')
guess = int(input('\nAdivinhe o nº entre 0 e 5 sorteado: '))
print('Analisando . . .')
sleep(1.5)
if guess == secret:
    print('Parabéns, você acertou!')
else:
    print(f'Você errou, {secret} era o certo.')

print('\n\nParabéns, você acertou!' if secret == guess else f'\n\nVocê errou, {secret} era o certo')
