# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 18

# Exercício 85: crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha separados os valores
# pares dos ímpares. No final, mostre valores pares e ímpares em ordem.
valores = [[], []]
for n in range(7):
    number = int(input(f"Digite o {n+1}º número: "))
    if number % 2:
        valores[1].append(number)
    else:
        valores[0].append(number)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram {valores[0]} e')
print(f'os valores ímpares digitados foram {valores[1]}')
