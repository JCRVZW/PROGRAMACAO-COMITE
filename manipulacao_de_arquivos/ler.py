try:
    with open ("dados.txt", "r") as arquivo:
        print (arquivo.read())
except FileNotFoundError:
    print("Arquivo não existente!")
