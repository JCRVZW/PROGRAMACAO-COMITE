def line():
    try:
        with open ("dados.txt","r") as arquivo:
            linhas = arquivo.readlines()
        total = len(linhas)
        print(f"O arquivo tem {total} linha(s)!")
    except FileNotFoundError:
        print("NAO EXISTE")
def main():
    line()
main()