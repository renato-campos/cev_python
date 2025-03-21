# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 19

# Exercício 90: faça um programa que leia o nome e a média de uma aluno
# guardando também a situação em uma dicionário, depois mostre o conteúdo
# da estrutura na tela

aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
for k, v in aluno.items():
    print(f"{k.title()} é igual a {v.title() if type(v) == 'class str' else v}")    # que linha linda ;)
