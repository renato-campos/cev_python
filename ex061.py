# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 61: refaça o desafio 051, lendo o primeiro termo e
# a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

termo = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
k = 1
while k <= 10:
    print(termo, end=' - ')
    termo += razao
    k += 1
print('fim')
