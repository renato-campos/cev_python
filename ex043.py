# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 43: desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela a seguir:
# < 18.5 abaixo do peso; entre 18.5 e 25 peso ideal; entre 25 e 30 sobrepeso;
# > 40 obesidade mórbida.

peso = float(input('Digite seu peso [kg]: '))
altura = float(input('Digite sua altura [m]: '))

imc = peso / altura ** 2

if imc <= 18.5:
    print(
        f'Seu IMC é {imc:.1f}, você está \033[1;31mabaixo do peso\033[0m recomendável')
elif imc <= 25:
    print(f'Seu IMC é {imc:.1f}, você está no \033[1;32mpeso ideal\033[0m')
elif imc <= 30:
    print(f'Seu IMC é {imc:.1f}, você está com \033[1;33msobrepeso\033[0m')
elif imc <= 40:
    print(f'Seu IMC é {imc:.1f}, você está \033[1;31mobeso\033[0m')
else:
    print(f'Seu IMC é {imc:.1f}, você tem \033[1;31mobesidade mórbida\033[0m')
