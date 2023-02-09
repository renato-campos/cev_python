# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 47: crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50.

for par in range(2, 51, 2):
    print(par, end=' ')
print('Acabou')

# Observações quanto ao custo computacional dos modos de fazer o ex047
for par in range(2, 51, 2):
    print(end=' . ')
    print(par, end=' ')
print('Acabou')

for par in range(2, 51):
    print(end=' . ')
    if par % 2 == 0:
        print(par, end=' ')
print('Acabou')
