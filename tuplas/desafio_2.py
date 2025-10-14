import random

lista = []

for i in range (6):
    lista.append(random.randint(1,12))
tuplo = ((lista[0], lista [1]), (lista [2], lista [3]), (lista [4], lista [5]))
tupla = tuple(tuplo)

print (type(tupla))
for x, y in tupla:
    print (f"ponto -> x={x}, y={y}")
