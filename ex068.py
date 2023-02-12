# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 15

# Exercício 68: faça um programa que jogue "par ou ímpar" com o computador.
# O programa será interrompido quando o jogador perder, mostrnado o total de
# vitórias consecutivas que ele conquistou.
from random import randint
from time import sleep

vitorias = 0
print('-=' * 20, f"{'Vamos jogar PAR ou ÍMPAR':^40}", '-=' * 20, sep='\n')
while True:
    pc = randint(1, 5)
    escolha = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    user = int(input('Digite seu número: '))
    sleep(0.5)
    resultado1 = pc + user
    if resultado1 % 2:
        resultado2 = 'I'
    else:
        resultado2 = 'P'
    print(f"""{'-' * 40}
Você jogou {user} e o computador {pc}
Totalizando {resultado1} que é {'PAR' if resultado2=='P' else 'ÍMPAR'}
{'-' * 40}""")
    sleep(0.5)
    if escolha == resultado2:
        print(
            f'Você \033[1;32mVENCEU!\033[0m\nVamos jogar novamente . . .\n{"-" * 40}')
        vitorias += 1
    else:
        print('Você \033[1;31mPERDEU\033[0m')
        break
print(f"{'-=' * 20}\nGAME OVER! Você venceu {vitorias} vezes")
