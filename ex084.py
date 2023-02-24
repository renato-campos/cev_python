# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 18

# Exercício 84: faça um programa que leia o nome e pessoa[1] de várias pessoas,
# guardando tudo em uma lista. No final, mostre: o número de pessoas,
# uma lista com as pessoas mais pesadas e uma com as mais leves.

pessoa = []
dados = []
leve = pesado = 0
while True:
    pessoa.append(str(input('Nome: ')).strip().capitalize())
    pessoa.append(int(input('Peso: ')))
    if leve == 0 and pesado == 0:
        leve = pesado = pessoa[1]
    elif pessoa[1] < leve:
        leve = pessoa[1]
    elif pessoa[1] > pesado:
        pesado = pessoa[1]
    pessoa.append(pessoa[1])
    dados.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo foram cadastradas {len(dados)} pessoas')
print(f'O maior peso] foi de {pesado} kg de: ', end='')
for p in dados:
    if p[1] == pesado:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {leve} kg de: ', end='')
for p in dados:
    if p[1] == leve:
        print(f'[{p[0]}]', end=' ')
