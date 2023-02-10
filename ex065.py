# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 14

# Exercício 65: crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer continuar a digitar valores.

soma = count = maior = menor = 0
resp = 'S'
while resp == 'S':
    number = int(input('Digite um número: '))
    soma += number
    count += 1
    if count == 1:
        maior = menor = number
    elif number > maior:
        maior = number
    elif number < menor:
        menor = number
    resp = str(input('Deseja continuar [S/N]: ')).replace(' ', '').upper()[0]
media = soma / count
print(f'''A soma dos {count} números deu {soma}
      com uma média dando {media:.2f},
      sendo o maior {maior} e o menor {menor}''')
