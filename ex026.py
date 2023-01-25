# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 09

# Exercício 26: faça um programa que leia uma frase pelo teclado e mostre:
# - quantas vezes aparece a letra 'A'
# - em que posição ela aparece a primeira vez
# - em que posição aparece a última vez

frase = input('Digite uma frase: ').strip().lower()
print(len(frase))
print(f'A letra "a" aparece {frase.count("a")} vezes')
print(f"Ela aparece a primeira vez na {frase.find('a') + 1}ª posição")
print(f"Ela aparece a ÚLTIMA vez na {len(frase) - (frase[::-1].find('a'))}ª posição")
