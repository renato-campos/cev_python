# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 15: escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60.00 por dia e R$0.15 por km rodado

km_percorrido = float(input('Qual o km percorrido? '))
dias_aluguel = int(input('Quantidade de dias alugado? '))

diaria = 60
vlr_km = 0.15

vlr_total = (dias_aluguel * diaria) + (km_percorrido * vlr_km)

print(f'Valor total do aluguel R${vlr_total:.2f}')
