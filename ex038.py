# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 38: escreva um programa que leia dois números inteiros e compare-os,
#  mostrando na tela uma mensagem de quem é maior, menor ou se são iguais.

number_1 = int(input('Digite um número: '))
number_2 = int(input('Digite outro número: '))

if number_1 > number_2:
    print(f'O {number_1} é maior e o é o {number_2} menor')
elif number_1 < number_2:
    print(f'O {number_2} é maior e o é o {number_1} menor')
else:
    print('Os números são iguais.')
