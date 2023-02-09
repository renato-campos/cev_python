# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 49: refaça o exercício 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for

number = int(input('Digite um número inteiro:'))

for k in range(11):
    print(f'{number:>2} x {k:>2} = {number * k:>3}')
