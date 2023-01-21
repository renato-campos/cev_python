# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 10: crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dólares ela pode comprar U$1.00 = R$5.15

cambio = 5.15
vlr_reais = float(input('Digite o valor em reais: R$ '))
vlr_dollars = vlr_reais / cambio

print(f'Com R${vlr_reais:.2f} você compra U${vlr_dollars:.2f}')
