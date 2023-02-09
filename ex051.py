# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 51: desenvolva um programa que leia o primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa progressão

termo_1 = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = 10

for k in range(termo_1, termo_1 + (termos - 1) * razao + 1, razao):
    print(k, end=' -> ')
print('Fim')
