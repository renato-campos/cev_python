# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 10

# Exercício 35: desenvolva um programa que leia o cumprimento de 3 retas e
# diga ao usuário se elas podem ou não formar um triângulo

lado1 = float(input('Digite a medida de uma das retas: '))
lado2 = float(input('Digite a medida de outra das retas: '))
lado3 = float(input('Digite a medida da última das retas: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print(
        f'Os lados de medidas {lado1}, {lado2} e {lado3} \033[0;32mpodem formar\033[0m um triângulo.')
else:
    print(
        f'Os lados de medidas {lado1}, {lado2} e {lado3}\033[31m NÃO formam\033[0m um triângulo.')
