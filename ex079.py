# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 17

# Exercício 79: crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = []
while True:
    resp = ' '
    number = int(input('Digite um número: '))
    if number in lista:
        print('Número repetido.')
        continue
    lista.append(number)
    while resp not in 'SYN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
print('*-' * 15)
print(f'Você digitou os seguintes valores: {lista}')
