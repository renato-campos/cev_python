# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 10

# Exercício 31: desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R0.50 por km para viagens até 200 km e
# R$0.45 para viagens mais longas.

price1 = 0.5
price2 = 0.45
limitador = 200
distancia = int(input('Qual a distância da viagem [km]: '))

if distancia <= limitador:
    ticket = distancia * price1
else:
    ticket = distancia * price2

print(f'O preço da passagem é R${ticket:.2f}')

ticket = distancia * price1 if distancia <= limitador else distancia * price2
print(f'O preço da passagem é R${ticket:.2f}')
