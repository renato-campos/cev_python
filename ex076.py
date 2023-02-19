# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 16

# Exercício 76: crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços na sequência. No final, 
# mostre uma listagem de preços, organizando os dados de forma tabular

mercado = ('arroz', 25.55, 'feijão', 12.25, 'bolacha', 3.55, 
           'café', 21.90, 'sabão', 17.33, 'leite', 7.88)

print(f'{"Produto":15}   {"Preço":^8}')
for k, v in enumerate(mercado):
    if k % 2 == 0:
        print(f'{v.title():.<15} R${mercado[k+1]:>8.2f}')
