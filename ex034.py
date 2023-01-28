# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 10

# Exercício 34: escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00 o aumento será de 10%, ou demais terão 15%

salario = float(input('Digite o salário: R$ '))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f'Para o salário de R${salario:.2f}\
\nO aumento será de R${aumento:.2f}\
\nResultando em um novo de \033[1;32mR${salario + aumento:.2f}\033[0m')
