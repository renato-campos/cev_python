# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 44: elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque 10% desc; à vista no crédito 5% desc;
# em 2x no crédito- normal; 3x ou + no cartão 20% juros

print(f'{"LOJAS TABAJARA":=^30}')
price = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista em dinheiro/débito/pix
[2] à vista no crédito
[3] 2x no crédito
[4] 3x ou mais no crédito
Qual é a sua opção: ''', end='')
forma_pag = int(input())
if forma_pag == 1:
    print(f'Sua compra de R${price:.2f} vai custar R${price * 0.9:.2f}')
elif forma_pag == 2:
    print(f'Sua compra de R${price:.2f} vai custar R${price * 0.95:.2f}')
elif forma_pag == 3:
    print(f'Sua compra de R${price:.2f} vai sair 2x de R$ {price / 2:.2f}')
elif forma_pag == 4:
    num_parcelas = int(input('Quantas parcelas: '))
    print(f'Sua compra será em {num_parcelas}x de R${price * 1.2 / num_parcelas:.2f} \
Sua compra de R${price:.2f} vai sair um total de R$ {price * 1.2:.2f}')
else:
    print('Opção inexistente. Tente novamente.')
