# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 17

# Exercício 81: crie um programa que vai ler vários números e colocar em uma
# lista. Depois mostre: quantos números foram digitados; a lista de valores
# ordenada de forma decrescente e se o valor 5 está na lista.

lista = []
while True:
    number = resp = " "
    while not number.isnumeric():
        number = str(input("Digite um número: "))
    lista.append(int(number))
    while resp not in 'SYN':
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'Os valores digitados foram: {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não consta na lista')
