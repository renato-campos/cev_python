# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 08

# Exercício 16: Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira.

from math import trunc

number = float(input('Digite um número decimal: '))


print(f'o número {number} tem a parte inteira {int(number)}')

print(f'O número {number} tem a parte inteira {trunc(number)}')
