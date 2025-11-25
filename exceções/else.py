def obtem_valor():
    try:
        valor = float(input("informe um número -> "))
    except ValueError:
        print("Valor invalido", end=' ')
        print("Necessário ser um número inteiro!")
    else:
        print(f"Valor informado é {valor}!")
        return int(input(f"Informe um valor -> "))
    
def main():
    obtem_valor

main()