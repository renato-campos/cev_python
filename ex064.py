# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 64: crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condição de
# parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles, desconsiderando a flag.
soma = count = 0
while True:
    number = int(input('Digite um número inteiro: [999 = sair] '))
    if number == 999:
        break
    soma += number
    count += 1
print(f'A soma dos {count} digitados é {soma}')
