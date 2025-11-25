def obtem_valor():
    try:
        valor = int(input("Informe um valor -> "))
    except ValueError:
        print("Valor invalido!", end=" ")
        print("Necessário ser inteiro!")
    else:
        print(f"Valor informado é {valor}")
    finally:
        print ("PROGRAMA ENCERRADO")

def main():
    obtem_valor()
main()