# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 10

# Exercício 33: faça um programa que leia 3 números e mostre
# qual é maior e qual é o menor

number1 = float(input('Digite um número: '))
number2 = float(input('Digite outro número: '))
number3 = float(input('Digite mais um número: '))

if number1 > number2:
    if number1 > number3:
        maior = number1
        if number2 > number3:
            menor = number3
        else:
            menor = number2
    else:
        maior = number3
        menor = number2
else:
    if number2 > number3:
        maior = number2
        if number1 > number3:
            menor = number3
        else:
            menor = number1
    else:
        maior = number3
        menor = number1

print(f'O maior número é {maior} e o menor é {menor}')

# outra lógica

if number1 > number2:
    maior = number1
    menor = number2
else:
    maior = number2
    menor = number1

if number3 > maior:
    maior = number3
else:
    if number3 < menor:
        menor = number3

print(f'O maior número é {maior} e o menor é {menor}')
