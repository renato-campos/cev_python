# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 09

# Exercício 23: faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos dígitos separados

# 1º modo - manipulação de strings
# ERRO se não existirem os 4 algarismos
# com os conhecimentos até aqui
number = input('Digite um número entre 0 e 9999: ')
print(f'unidade: {number[3]}')
print(f'dezena:  {number[2]}')
print(f'centena: {number[1]}')
print(f'milhar:  {number[0]}')

# 2º modo - aritmética
number = int(number)
unidade = number % 10
print(f'unidade: {unidade}')
dezena = (number - unidade) // 10 % 10
print(f'dezena:  {dezena}')
centena = (number - dezena*10 - unidade) // 100 % 10
print(f'centena: {centena}')
print(f'milhar:  {number // 1000}')

# 3º modo - aritmética
milhar = number // 1000
_ = number - milhar * 1000
centena = _ // 100
_ -= centena * 100
dezena = _ // 10
unidade = _ - dezena * 10
print(f'unidade: {unidade}')
print(f'dezena:  {dezena}')
print(f'centena: {centena}')
print(f'milhar:  {milhar}')
