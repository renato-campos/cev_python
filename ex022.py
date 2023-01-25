# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 09

# Exercício 22: crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiúsculas
# - o nome com todas as letras minúsculas
# - quantas letras ao todo - sem considerar espaços
# - quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()

print(f'Seu nome em letras maiúsculas: {nome.upper()}')
print(f'Seu nome em letras maiúsculas: {nome.lower()}')
print(f'Número de letras no nome: {len(nome) - nome.count(" ")}')
print(f'Número de letras do 1º nome: {nome.find(" ")}')
