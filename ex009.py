# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 09: faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

number = int(input('Digite um número para ver sua tabuada: '))

print(f'''
Tabuada do {number}
{13 * '-'}
{number:>2} x  0 = {number * 0:>3}
{number:>2} x  1 = {number * 1:>3}
{number:>2} x  2 = {number * 2:>3}
{number:>2} x  3 = {number * 3:>3}
{number:>2} x  4 = {number * 4:>3}
{number:>2} x  5 = {number * 5:>3}
{number:>2} x  6 = {number * 6:>3}
{number:>2} x  7 = {number * 7:>3}
{number:>2} x  8 = {number * 8:>3}
{number:>2} x  9 = {number * 9:>3}
{number:>2} x 10 = {number * 10:>3}
''')
