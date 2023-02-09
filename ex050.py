# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 50: desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
count = 0
soma_par = 0
for k in range(6):
    number = int(input(f'Digite o {k+1}º número inteiro: '))
    if number % 2 == 0:
        soma_par += number
        count += 1

print(f'A soma dos {count} números pares é {soma_par}')
