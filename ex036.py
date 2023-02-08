# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 36: escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado.

vlr_imovel = float(input('Digite o valor do imóvel: R$ '))
renda = float(input('Digite a renda mensal: R$ '))
tempo = int(input('Prazo em anos do financiamento: '))
vlr_parcela = vlr_imovel / (tempo * 12)
if vlr_parcela < (renda * 0.3):
    print(
        f'Seu financiamento foi \033[1;32maprovado\033[0m\nValor da parcelas de R${vlr_parcela:.2f}\nNº de parcelas {tempo * 12}x')
else:
    print(
        f'Seu financiamento foi \033[1;33mrecusado\033[0m\nValor da parcela R${vlr_parcela:.2f} é muito elevado')
