# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 62: melhore o exercício 61,perguntando ao usuário
# se ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
k = 1
n = 10
while k <= n:
    print(termo, end=' - ')
    termo += razao
    k += 1
    if k > n:
        n += int(input('\nQuantos termos mais deseja mostrar: '))

print('fim')
