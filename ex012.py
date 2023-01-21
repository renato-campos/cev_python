# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 12: faça um algoritmo que leia o preço de um produto e mostre seu novo preço com um desconto de 5%

price = float(input('Digite o preço normal: R$ '))
discont_perc = 5

new_price = price * (1 - discont_perc / 100)

print(f'O preço atual com {discont_perc}% de desconto é R${new_price:.2f}')
