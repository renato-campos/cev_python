# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 17

# Exercício 78: faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista. No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.
lista = []
for k in range(5):
    lista.append(int(input(f'Digite um número para posição {k}: ')))

maior = max(lista)
menor = min(lista)

print(f'O maior valor digitado foi o {maior} nas posições: ', end=" ")
pos = 0
for k in range(lista.count(maior)):
    pos = lista.index(maior, pos)
    print(pos, end=' ')
    pos += 1

print(f'\nO menor valor digitado foi o {menor} nas posições: ', end=" ")
pos = 0
for k in range(lista.count(menor)):
    pos = lista.index(menor, pos)
    print(pos, end=' ')
    pos += 1
