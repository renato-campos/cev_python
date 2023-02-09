# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 56: desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo
# Nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

soma = idd_velho = k_mulher = 0
nome_velho = ''

for pessoa in range(4):
    print(f'----- {pessoa+1}ª pessoa -----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    soma += idade
    if sexo == 'M' and idade > idd_velho:
        idd_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        k_mulher += 1

print(f'''\nA média de idade do grupo é de {soma / 4:.1f} anos
O homem mais velho tem {idd_velho} anos e se chama {nome_velho}
Temos {k_mulher} mulheres menores de 20 anos.''')
