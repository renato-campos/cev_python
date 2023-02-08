# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 37: escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 binário, 2 octal, 3 hexadecimal

number = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
OPÇÃO -> ''', end=' ')
option = int(input())

if option == 1:
    print(f'{number} em BINÁRIO é {bin(number)[2:]}')

elif option == 2:
    print(f'{number} em OCTAL é {oct(number)[2:]}')

elif option == 3:
    print(f'{number} em BINÁRIO é {hex(number)[2:]}')
else:
    print('Opção incorreta, inicie novamente.')
