# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 08: escreva um programa que leia um valor em metros e o exiba convertido da milímetros a quilômetros

medida = float(input('Digite uma medida em metros: '))

print(f'''
{medida / 1000:.3f} quilômetros
{medida / 100:.3f} hectômetros
{medida / 10:.3f} decâmetros
{medida * 10:.2f} decímetros
{medida * 100:.2f} centímetros
{medida * 1000:.2f} milímetros
''')
