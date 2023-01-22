# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 08

# Exercício 20: o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = [input('Digite o nome do 1º aluno: '),
          input('Digite o nome do 2º aluno: '),
          input('Digite o nome do 3º aluno: '),
          input('Digite o nome do 4º aluno: ')]

random.shuffle(alunos)

print(f'A ordem de apresentação será {alunos}')
