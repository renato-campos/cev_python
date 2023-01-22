# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 08

# Exercício 17: faça um programa que leia o tamanho do cateto oposto e do adjacente de um triângulo retângulo, calcule e mostre o tamanho da hipotenusa

import math

cateto_oposto = float(input('Digite a medida do cateto oposto: '))
cateto_adjacente = float(input('Digite a medida do cateto adjacente: '))

print(
    f'A hipotenusa desse triângulo mede {math.hypot(cateto_oposto, cateto_adjacente):.2f}')

print(
    f'A hipotenusa desse triângulo mede {math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2):.2f}')
