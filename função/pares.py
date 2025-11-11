list = []
def lista ():
    while True:
        listas = int(input("Informe os números (ou 909 para sair) -> "))
        if listas %2 == 0:
            list.append (listas)
        if listas == 909:
            break
    for num in list:
        print(num, "é par!")
def main ():
    lista()
main()

