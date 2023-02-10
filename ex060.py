# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 60: faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial
numero = int(input('Digite um número: '))
k = numero
fatorial = 1
while k > 0:
    fatorial *= k
    k -= 1
print(f'{numero}! é igual a {fatorial}')


fact = factorial(numero)
print(fact)
