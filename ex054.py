# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 54: crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import datetime
maiores = 0
menores = 0

limite = datetime.today().year - 18

for k in range(7):
    ano = int(input('Digite o ano de nascimento: '))
    if ano > limite:
        menores += 1
    else:
        maiores += 1
print(f'Tivemos {menores} menores de idade\ne {maiores} maiores de idade')
