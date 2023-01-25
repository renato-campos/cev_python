# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 09

# Exercício 24: Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "Santo"

cidade = input('Digite o nome da cidade:').strip().title()
print(f'O nome da cidade começa com "Santo"? \
{str(("Santo" in cidade[0:5])).replace("True", "Sim").replace("False", "Não")}')
