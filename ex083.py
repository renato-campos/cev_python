# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 17

# Exercício 83: crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite a expressão algébrica: '))
parenteses = 0
for p in expressao:
    if p == '(':
        parenteses += 1
        continue
    elif p == ')':
        parenteses -= 1
    if parenteses < 0:
        break

if parenteses:
    print('Expressão inválida!')
else:
    print('Expressão válida!')
