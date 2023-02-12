# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 15

# Exercício 70: crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário que continuar e no final, mostre:
# O total da compra, quantos produtos custam mais de $1000 e qual o mais barato

total = count = mais1000 = barato_vlr = 0
barato_nome = ''

while True:
    produto = str(input('Qual o produto: ')).strip().title()
    preco = float(input('Qual o preço: R$ '))
    count += 1
    total += preco

    if preco > 1000:
        mais1000 += 1

    if preco < barato_vlr or count == 1:
        barato_vlr = preco
        barato_nome = produto

    while resp not in 'SYN':
        resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f"""{'-=' * 20}
O valor total da compra dos {count} produtos resultou R$ {total:.2f}
Sendo {mais1000} produtos custando mais de R$ 1.000,00
e o mais barato de todos foi {barato_nome} por R$ {barato_vlr:.2f}""")
