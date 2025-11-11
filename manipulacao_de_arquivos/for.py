try:
    with open ("dados.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha)
except FileNotFoundError:
    print("SEM ARQUIVO!!!")