# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 14: escreva um programa que converta uma temperatura digitada em °C e converta para °F

celsius = float(input('Digite a temperatura em °C: '))

farenheit = celsius * 9 / 5 + 32

print(f'{celsius:.1f}°C  >>>  {farenheit:.1f}°F')
