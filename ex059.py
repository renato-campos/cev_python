# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 59: crie um programa que leia 2 valores e mostre um menu na tela
# com as opções 1 somar, 2 multiplicar, 3 maior, 4 novos números e 5 sair.
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 4

while opcao != 5:
    if opcao == 1:
        print(f'A soma de {num1} e {num2} é {num1 + num2}')
    elif opcao == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior é {num1}')
        elif num2 > num1:
            print(f'O maior é {num2}')
        else:
            print('Eles são iguais')
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif opcao == 5:
        break
    else:
        print('Opção incorreta, tente novamente')
    print('''Operações:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Digite sua opção: '))
print('Finalizado.')
