# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 08

# Exercício 19: um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

alunos = [input('Digite o nome do 1º aluno: '),
          input('Digite o nome do 2º aluno: '),
          input('Digite o nome do 3º aluno: '),
          input('Digite o nome do 4º aluno: ')]

print(f'O aluno escolhido foi {choice(alunos)}')
