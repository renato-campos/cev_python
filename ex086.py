# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 18

# Exercício 86: crie um programa que crie uma matriz de dimensão 3x3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela, com a
# formatação correta.

matriz = [[],
          [],
          []]

for linha in range(3):
    for coluna in range(3):
        elemento = int(input(f'Digite o elemento da posição {linha}x{coluna}: '))
        matriz[linha].append(elemento)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:>4}]', end=' ')
    print()
