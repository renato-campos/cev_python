# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 17

# Exercício 82: crie um programa que vai ler vários números e colocar em uma
# lista. Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os ímpares digitados, respectivamente. Ao final, mostre as 3 listas.

lista = []
pares = []
impares = []
while True:
    number = int(input('Digite um número: '))
    lista.append(number)
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
for v in lista:
    if v % 2:
        impares.append(v)
    else:
        pares.append(v)
print(f'''A lista completa é {lista}
A lista de pares é {pares}
A lista de ímpares é {impares}''')
