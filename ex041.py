# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 41: a CBDA precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade: até 9 anos - mirim, até 14 anos infantil,
# até 19 anos - junior, até 25 anos - sênior, acima - master

from datetime import datetime

idade = datetime.today().year - int(input('Ano de nascimento: ').strip())
if idade <= 9:
    print(f'O atleta tem {idade} anos\nCategoria \033[1;31mMIRIM\033[0m')
elif idade <= 14:
    print(f'O atleta tem {idade} anos\nCategoria \033[1;31mINFANTIL\033[0m')
elif idade <= 19:
    print(f'O atleta tem {idade} anos\nCategoria \033[1;31mJÚNIOR\033[0m')
elif idade <= 25:
    print(f'O atleta tem {idade} anos\nCategoria \033[1;31mSÊNIOR\033[0m')
else:
    print(f'O atleta tem {idade} anos\nCategoria \033[1;31mMASTER\033[0m')
