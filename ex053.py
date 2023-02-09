# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 53: crie um programa que leia uma frase qualquer
# e diga se ela é um palindromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
inverso = frase[::-1]

print(f'O inverso da palavra {frase} é {inverso}')

if inverso == frase:
    print('Ela é um palíndromo')
else:
    print('Ela não é um palíndromo')
