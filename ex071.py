# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 15

# Exercício 71: crie um programa que simule o funcionamento de um caixa
# eletrônico. No início, pergunte ao usuário qual o valor a ser sacado
# e o programa vai informar quantas cédulas de cada valor serão entregues
# O caixa possui cédulas de 50, 20, 10 e 1

print(f"""{'=' * 30}
{'Banco':^30}
{'=' * 30}""")
valor_sacado = int(input('Digite o valor a sacar: R$ '))
resto = valor_sacado
ced_50 = ced_20 = ced_10 = ced_01 = 0
while resto != 0:
    if resto >= 50:
        ced_50 = resto // 50
        resto %= 50
    elif resto >= 20:
        ced_20 = resto // 20
        resto %= 20
    elif resto >= 10:
        ced_10 = resto // 10
        resto %= 10
    else:
        ced_01 = resto
        resto %= 1
print(f"""cédulas de R$ 50,00 --> {ced_50:>3}
cédulas de R$ 20,00 --> {ced_20:>3}
cédulas de R$ 10,00 --> {ced_10:>3}
cédulas de R$  1,00 --> {ced_01:>3}
{'=' * 30}
Volte sempre!""")

# Lógica usada para simplificar o código
print('\n\n')
resto = valor_sacado
cedula = 50
while True:
    num_cedulas = 0
    if resto >= cedula:
        num_cedulas = resto // cedula
        resto %= cedula
        if num_cedulas > 0:
            print(f'cédulas de R$ {cedula:>5.2f} --> {num_cedulas:>3}')
    else:
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
    if resto == 0:
        break
print(f"{'=' * 30}\nVolte sempre!")
