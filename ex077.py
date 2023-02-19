# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 16

# Exercício 77: crie um programa que tenha uma tupla com várias palavras,
# não usar acentos. Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

palavras = ('tres', 'mulheres', 'sendo', 'uma', 'delas', 'idosa', 'dois',
            'homens', 'criança', 'estavam', 'dentro', 'equipamento', 'que',
            'parou', 'funcionar', 'apos', 'queda', 'energia', 'testemunha',
            'disse', 'grupo', 'estava', 'muito', 'nervoso', 'ofegante')

for palavra in palavras:
    print(f'\n{palavra}: ', end='')
    for letra in palavra:
        if letra in ('a', 'e', 'i', 'o', 'u'):
            print(letra, end=' ')
