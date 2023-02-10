# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 63: escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.

termos = int(input('Digite o número de termos da sequência de Fibonacci a exibir: '))
k = 1
while k <= termos:
    if 1 <= k <= 2:
        fib1 = 1
        fib2 = 1
    else:
        fib1, fib2 = fib2, fib2 + fib1
    print(fib2, end=' - ')
    k += 1
print('fim')
