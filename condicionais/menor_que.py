numero_1 = int(input("informe o primero numero -> "))
numero_2 = int(input("informe o primero numero -> "))

if numero_1<numero_2:
    print(f"{numero_1} é menor!")
elif numero_2<numero_1:
    print (f"{numero_2} é menor!")
else:
    print ("Os números são iguais!")