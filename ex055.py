# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 55: faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos

pesado = 0
leve = 0

for k in range(5):
    peso = float(input('Digite o peso da pessoa: '))
    if k == 0:
        pesado = leve = peso
    elif peso > pesado:
        pesado = peso
    elif peso < leve:
        leve = peso
print(f'O maior peso foi de {pesado:.2f}kg e o mais leve foi de {leve:.2f}kg')
