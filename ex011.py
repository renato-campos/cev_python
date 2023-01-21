# CeV - Curso em Vídeo
# Prof. Gustavo Guanabara

# Aluno: Renato

# Exercícios da Aula 07

# Exercício 11: faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Digite a largura da parede [metros]: '))
altura = float(input('Digite a altura da parede [metros]: '))
area_parede = largura * altura
qtde_tinta = area_parede / 2

print(
    f'Uma parede de {area_parede:.2f} m² de área\nprecisa de {qtde_tinta:.2f} litros de tinta para ser pintada')
