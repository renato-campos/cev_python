# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 18

# Exercício 89: crie um programa que leia o nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim contendo a
# média de cada um e permita que o usuário possa mostrar as notas de cada
# aluno individualmente

colegio = []
notas = []
resp = ''
while resp != 'N':
    nome = str(input('Nome:')).strip().capitalize()
    for n in range(2):
        nota = float(input(f'Nota {n+1}: '))
        notas.append(nota)
    media = (notas[0]+notas[1])/2            # fazendo o append direto com a lista composta
    colegio.append([nome, notas[:], media])
    notas.clear()
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

print('-=' * 20)
print(f"{'nº:':<4} {'Nome:':<20} {'Média:':6}")
for n in range(len(colegio)):
    print(f"{n:4} {colegio[n][0]:<20} {colegio[n][2]:>6.1f}")
while True:
    print('-=' * 20)
    pesquisa = int(input('Mostrar notas de qual aluno? [999-sair] '))
    if pesquisa == 999:
        print('Encerrando...')
        break
    elif pesquisa >= len(colegio):
        continue
    print(f'As notas de {colegio[pesquisa][0]} são {colegio[pesquisa][1]}')
print('<<< VOLTE SEMPRE >>>')
