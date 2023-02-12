# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 15

# Exercício 69: crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
# não continuar e no final, mostre: quantos tem mais de 18, quantos homens
# cadastrados e quantas mulheres têm menos de 20.

count = maiores = homens = mulheres20 = 0
while True:
    resp = idade = sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while not idade.isnumeric():
        idade = input('Idade: ')
    idade = int(idade)
    count += 1
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres20 += 1
    if idade > 18:
        maiores += 1
    while resp not in 'SYN':
        resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f"""Dentre as {count} pessoas cadastradas,
{maiores} eram pessoas maiores de 18 anos,
{mulheres20} eram mulheres com menos de 20 anos
e {homens} eram homens""")
