# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 10

# Exercício 32: faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date

ano = int(input('Digite o ano ou 0 para o atual: '))
if ano == 0:
    ano = date.today().year
flag = False

if ano > 1528 and ano % 4 == 0:
    flag = True
    if ano % 100 == 0:
        flag = False
        if ano % 400 == 0:
            flag = True

print(f'O ano {ano}', 'é bissexto' if flag else 'não é bissexto')
