# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 10

# Exercício 30: crie um programa que leia um número inteiro e
# mostre na tela se ele é PAR ou ÍMPAR

number = int(input('Digite um número inteiro: '))

if number % 2:
    print(f'O número {number} é ÍMPAR')
else:
    print(f'O número {number} é PAR')
