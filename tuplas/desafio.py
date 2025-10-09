import random

lista = []
unica = []
for i in range (20):
    lista.append(random.randint(1,20))

for numero in lista:
    if numero not in unica:
        unica.append(numero)
tupla = tuple(unica)

print (*lista)
print (*unica)
print (type(tupla))