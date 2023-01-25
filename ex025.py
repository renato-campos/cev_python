# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 09

# Exercício 25: crie um programa que leia o nome de uma pessoa e
# diga se ela tem Silva no nome

nome = str(input('Digite o nome completo: ')).strip().title()
print(f'A pessoa tem Silva no nome? \
{str("Silva" in nome.split()).replace("True", "Sim").replace("False", "Não")}')
