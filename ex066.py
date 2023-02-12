# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 15

# Exercício 66: crie um programa que leia vários números inteiros pelo teclado
# O programa só vai parar quando o usuário digitar 999, que é a condição de
# parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles, desconsiderando o flag.
soma = count = 0
while True:
    numero = int(input('Digite um número [999 para sair]: '))
    if numero == 999:
        break
    soma += numero
    count += 1
print(f'Foram digitados {count} números cuja soma é {soma}')
