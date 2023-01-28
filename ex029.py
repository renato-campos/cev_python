# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 10

# Exercício 29: escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar a velocidade de 80 km/h, mostre uma mensagem
# dizendo que ele foi multado.
# A multa vai custar $7,00 por cada km acima do limite.

limit = 80
vlr_multa = 7

speed = int(input('Digite a velocidade do veículo: '))

if speed > limit:
    tot_multa = (speed - limit) * vlr_multa
    print(f'''VOCÊ FOI MULTADO!
Sua velocidade é de {speed} Km/h
Excedendo o limite em {speed - limit} Km/h
O valor da multa é de R${tot_multa:.2f}''')

print('\nDirija com segurança!')
