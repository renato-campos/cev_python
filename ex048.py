# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 13

# Exercício 48: faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0            # acumuladores somam os números
contador = 0        # contador, conta
for k in range(3, 500, 3):
    if k % 2:
        contador += 1
        soma += k
print(f'O somatório dos {contador} números deu {soma}')
