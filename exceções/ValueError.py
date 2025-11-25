def obtem_valor():
    return int(input("Digite um valor -> "))

def main():
    try:
        valor = obtem_valor()
    except ValueError:
        print("Valor inválido,", end =" ")
        print("Precisa ser um número inteiro!")
    else:
        print(f"Você digitou o valor {valor}!")

main()