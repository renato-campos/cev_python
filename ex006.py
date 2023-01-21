# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 06: crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada

number = int(input('Digite um número: '))

print(f'''Dado o número {number}
    tem {2 * number} como seu dobro,
    tem {3 * number} como seu triplo
    e {number ** 0.5:.2f} como sua raiz quadrada''')
