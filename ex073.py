# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 16

# Exercício 73: crie uma tupla preenchida com os 20 primeiros colocados da
# tabela do Brasileirão, na ordem de colocação. Depois mostre:
# os 5 primeiros, os 4 últimos, os times em ordem alfabética e qual a 
# classificação de um time específico.

tabela = ('Palmeiras',
          'Internacional',
          'Fluminense',
          'Corinthians',
          'Flamengo',
          'Athletico-PR',
          'Atlético-MG',
          'Fortaleza',
          'São Paulo',
          'América-MG',
          'Botafogo',
          'Santos',
          'Goiás',
          'Red Bull Bragantino',
          'Coritiba',
          'Cuiabá',
          'Ceará',
          'Atlético-GO',
          'Avaí',
          'Juventude')
print('\033[1mClassificação do Brasileirão:\033[0m')
for pos, time in enumerate(tabela):
    print(f'{pos+1}º -> {time}')
print('-*' * 20)
print('\033[1mOs 5 primeiros colocados:\033[0m')
for time in tabela[:6]:
    print(time)
print('-*' * 20)
print('\033[1mOs 4 últimos colocados:\033[0m')
for time in tabela[-4:]:
    print(time)
print('-*' * 20)
print('\033[1mOs times em ordem alfabética:\033[0m')
for time in sorted(tabela):
    print(time)
print('-*' * 20)
time = str(input('Qual time você deseja consultar: ')).strip()
print(f'{time} está na posição: {tabela.index(time)+ 1}')
