tupla = ((12,45), ("Romero", "Britto"))

print (tupla[1][1])

###################

matriz = ((1,2,3), (4,5,6),(7,8,9))
print (matriz[1][1])

for linha in matriz:
    for coluna in linha:
        print (coluna, end=' ')
    print ()