# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 15

# Exercício 67: faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O programa será
# interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('\nTabuada de qual número: '))
    if numero < 0:
        break
    print(f'\nTabuada do {numero}\n{"-" * 14}')
    for k in range(11):
        print(f"{numero:>2} x {k:>2} = {numero * k:>3} ")
    print(f'{"-" * 14}')
print('\nPrograma encerrado.')
