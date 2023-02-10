# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 57: faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado peça a digitação novamente até ter um valor correto.

sexo = ' '

while sexo not in 'FM':
    sexo = str(input('Digite o sexo [M/F]: ')).replace(' ', '').upper()[0]
print(sexo)
