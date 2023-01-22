# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 08

# Exercício 18: faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angle_degrees = float(input('Digite a medida de um ângulo em graus: '))

angle_radians = math.radians(angle_degrees)

print(f'''O ângulo {angle_degrees}° tem:
seno igual a {math.sin(angle_radians):.2f}
cosseno igual a {math.cos(angle_radians):.2f}
tangente igual a {math.tan(angle_radians):.2f}''')

# observe que retornou resultado para tangente de 90°
