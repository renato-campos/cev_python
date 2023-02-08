# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 40: crie um programa que leia duas notas de um aluno e
# calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# até 7.0 aprovado, menos de 7.0 e até 5.- recuperação e menos de 5.0 reprovado

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2)/2

if media >= 7:
    print(
        f'Com as notas {nota1} e {nota2} obteve média {media:.1f}\nO aluno está \033[1;32mAPROVADO\033[0m')
elif 7.0 > media >= 5.0:
    print(
        f'Com as notas {nota1} e {nota2} obteve média {media:.1f}\nO aluno está \033[1;33mRECUPERAÇÃO\033[0m')
else:
    print(
        f'Com as notas {nota1} e {nota2} obteve média {media:.1f}\nO aluno está \033[1;31mREPROVADO\033[0m')
