# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 18

# Exercício 87: aprimore o exercício anterior mostrando: a soma de todos os
# valores pares digitados, a soma dos valores da terceira coluna e o maior
# valor da segunda linha.
matriz = [[],
          [],
          []]
soma_par = coluna3 = maior2l = 0

for linha in range(3):
    for coluna in range(3):
        elemento = int(input(f'Digite o elemento da posição {linha}x{coluna}: '))
        matriz[linha].append(elemento)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:>4}]', end=' ')
        if not matriz[linha][coluna] % 2:
            soma_par += matriz[linha][coluna]
        if coluna == 2:
            coluna3 += matriz[linha][2]
        if matriz[1][coluna] > maior2l:
            maior2l = matriz[1][coluna]
    print()

print(f'\n\nA soma dos valores pares da matriz é {soma_par}')
print(f'A soma dos valores da 3ª coluna é {coluna3}')
print(f'O maior valor da 2ª linha é {maior2l}')
