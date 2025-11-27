def ler_elemento(lista):
    try:
        indice = int(input("Digite o índice que deseja acessar -> "))
        elemento = lista[indice]
        print(f"Elemento no índice {indice} -> {elemento}")
    except IndexError:
        print("índice fora de lista!")
    except ValueError:
        print("você deve digitar um número inteiro!")

listas = [10, 20, 30, 40]

def main():
    ler_elemento(listas)
main()
