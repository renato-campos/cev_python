# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 16

# Exercício 74: crie um programa que vai gerar cinco números aleatórios e
# colocar em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
for x in tupla:
    print(x, end=' ')
print('\nO maior valor sorteado foi: ', max(tupla))
print('O menor valor sorteado foi: ', min(tupla))
