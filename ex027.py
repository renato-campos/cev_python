# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 09

# Exercício 27: faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente

nome = input('Digite o nome completo: ').strip().title()
# nome = nome.split()
print('Primeiro nome = ', nome.split()[0])
print('Último nome = ', nome.split()[-1])
