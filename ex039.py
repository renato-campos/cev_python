# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 39: faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se já é hora de se alistar ou se já passou da hora. Deve mostrar também o tempo faltante ou que passou para o alistamento.

from datetime import datetime

ano_nasc = int(input('Digite seu ano de nascimento: '))
hoje = datetime.today().year
idade = hoje - ano_nasc
if idade < 18:
    print(f'''Quem nasceu em {ano_nasc} tem {idade} anos em {hoje}
Ainda faltam {18 - idade} anos para seu alistamento
que será em {hoje + (18 - idade)}''')
elif idade > 18:
    print(f'''Quem nasceu em {ano_nasc} tem {idade} anos em {hoje}
Já se passaram {idade - 18} anos do alistamento
que foi em {hoje - (idade - 18)}''')
else:
    print(f'''Você tem {hoje - ano_nasc} anos
Deve se alistar imediatamente''')
