lista = []
try:
    with open ("Frutas.txt", "r") as arquivo:
         arquivo.read()

    for fruta in arquivo:
        lista.append(fruta)
    print(fruta)

except FileNotFoundError:
    print("ARQUIVO NADA!!!")
