# Curso de Python 3 - Mundo 1: Fundamentos
# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 06

# Exercício 04: faça um programa que leia algo pelo teclado e mostre o seu tipo
# primitivo e todas as informações possíveis sobre ele.

texto = input('Digite algo: ')
print('testa se é alfanumérico', texto.isalnum())
print('testa se é alfabético', texto.isalpha())
print('testa se é ASCII', texto.isascii())
print('testa se é decimal', texto.isdecimal())
print('testa se é digito', texto.isdigit())
print('testa se é identificador', texto.isidentifier())
print('testa se é minúscula', texto.islower())
print('testa se é número', texto.isnumeric())
print('testa se é imprimível', texto.isprintable())
print('testa se é espaço', texto.isspace())
print('testa se é formato de título',texto.istitle())
print('testa se é maiúscula',texto.isupper())
