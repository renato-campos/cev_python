# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 52: faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.

number = int(input('Digite um número: '))

count = 0

for k in range(1, number+1):
    if number % k:
        print(f'\033[31m{k}\033[0m', end=' ')
    else:
        count += 1
        print(f'\033[32m{k}\033[0m', end=' ')
print(f'\nO número {number} foi divisível {count} vezes')

if count > 2:
    print('e por isso ele \033[1;31mNÃO É PRIMO!\033[0m')
else:
    print('e por isso ele \033[1;32mÉ PRIMO!\033[0m')
