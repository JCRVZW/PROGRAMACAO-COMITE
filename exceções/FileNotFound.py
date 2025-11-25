def ler_arquivo (nome_arquivo):
    try:
        with open (nome_arquivo, "r") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo não encontrado!")

def main():
    ler_arquivo("LOGS_EMPRESA.txt")

main()