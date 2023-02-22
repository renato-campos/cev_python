# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 17

# Exercício 80: crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta de inserção,
# sem usar o sort(). No final, mostre a lista ordenada na tela.

lista = []
for k in range(5):
    number = int(input(f'Digite o {k+1}º número: '))

    if k != 0:
        for pos in range(len(lista)):
            if number <= lista[pos]:
                lista.insert(pos, number)
                print(f'Adicionado na posição {pos} da lista...')
                break
            elif pos == len(lista)-1:
                print('Adicionado ao final da lista...')
                lista.append(number)
    else:
        lista.append(number)
        print('Iniciando a lista...')

print(lista)
