# CeV — Curso em Vídeo
# Prof. Gustavo Guanabara
# Aluno: Renato

# Exercícios da Aula 12

# Exercício 42: refaça o exercício 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado: equilátero, isósceles, escaleno

lado1 = float(input('Digite a medida do lado 1: ').strip())
lado2 = float(input('Digite a medida do lado 2: ').strip())
lado3 = float(input('Digite a medida do lado 3: ').strip())

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:

    # na igualdade temos que se a=b e b=c então a=c
    if lado1 == lado2 == lado3:
        print('Essas medidas formam um triângulo \033[1;32mEquilátero\033[0m')

    # na desigualdade essa inferência não ocorre, deve-se testar se c!=a
    elif lado1 != lado2 != lado3 != lado1:
        print('Essas medidas formam um triângulo \033[1;32mEscaleno\033[0m')
    else:
        print('Essas medidas formam um triângulo \033[1;32mIsóceles\033[0m')
else:
    print('Esses segmentos \033[1;31mNÃO FORMAM\033[0m um triângulo.')
