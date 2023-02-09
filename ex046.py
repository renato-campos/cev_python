# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 46: faça um programa que mostre na tela uma contagem regressiva 
# para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa
# de 1 segundo entre eles.

from time import sleep

for k in range(10, 0, -1):
    print(k)
    sleep(0.5)
print('Feliz Ano Novo!')
