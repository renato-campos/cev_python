# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 07: desenvolva um programa que leia as duas notas d um aluno, calcule e mostre a sua média

# Entrada das notas
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

# Cálculo da média
media = (nota_1 + nota_2) / 2

# Saída dos resultados
print(f'Com notas {nota_1} e {nota_2} o aluno obteve média {media:.1f}')
