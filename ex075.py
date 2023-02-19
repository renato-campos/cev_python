# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 16

# Exercício 75: desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# quantas vezes apareceu o 9
# em que posição pareceu o primeiro valor 3
# quais foram os pares

minha_tupla = (int(input('Digite um número inteiro: ')),
               int(input('Digite um número inteiro: ')),
               int(input('Digite um número inteiro: ')),
               int(input('Digite um número inteiro: ')))

count9 = 0
for v in minha_tupla:
    if v == 9:
        count9 += 1
print(f'O nº 9 apareceu {count9} vezes')
print('O nº 3 apareceu a primeira vez na posição: ', minha_tupla.index(3))
print('O números pares foram: ', end=' ')
for v in minha_tupla:
    if v % 2 == 0:
        print(v, end=' ')
