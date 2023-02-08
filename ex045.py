# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 45: crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

computer = randint(0, 2)

print(f'{"JOKEMPÔ":=^25}')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

user = int(input('Qual a sua jogada: '))

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
sleep(0.5)

print(f'''{'-=' * 30}
Computador jogou {computer}
Usuário jogou {user}
{'-=' * 30}''')
if computer == user:
    print('\033[1;33mEMPATE\033[0m')
elif (computer == 0 and user == 1)\
        or (computer == 1 and user == 2)\
        or (computer == 2 and user == 0):
    print('\033[1;32mUSUÁRIO VENCE\033[0m')
else:
    print('\033[1;31mCOMPUTADOR VENCE\033[0m')
