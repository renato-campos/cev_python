# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 13: faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com um aumento de 15%

raise_perc = 15

salary = float(input('Digite seu salário: R$ '))

salary *= (1 + (raise_perc/100))

print(
    f'Com um aumento de {raise_perc}%, o novo salário será de R${salary:.2f}')
