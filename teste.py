A = [1, 2, 3, 4, 5, 6]
B = [10, 20, 30, 40, 50, 60]
lista = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7]]
if A not in lista:
    lista.append(A)
if B not in lista:
    lista.append(B)
print(lista)