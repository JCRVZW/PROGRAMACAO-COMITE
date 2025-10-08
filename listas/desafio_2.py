lista = [1,2,3,4,5,6,7,8,9,10]
pares = []

for numero in lista:
    if numero %2 == 0:
        pares.append(numero)

print (f"lista original -> {lista}")
print (f"lista de números pares -> {pares}") 

###########################

import random

lista1 = []
pares1 = []

for i in range (10):
    lista1.append(random.randint(1,100))

for i in lista1:
    if i % 2 == 0:
        pares1.append (i)

print (f"lista original -> {lista1}")
print (f"lista de números pares -> {pares1}") 