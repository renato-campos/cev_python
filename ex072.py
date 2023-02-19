# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 16

# Exercício 72: crie um programa que tenha um tupla totalmente preenchida
# com uma contagem por extenso de zero a vinte. Seu programa deverá ler um
# número pelo teclado, entre 0 e 20, e mostrá-lo por extenso.

num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
               'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
               'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
               'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número inteiro [0 a 20]: '))
    if 0 <= numero <= 20:
        break
print(f'\nO número digitado foi o {num_extenso[numero]}')