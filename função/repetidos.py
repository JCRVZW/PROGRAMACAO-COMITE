def main ():
    listaF = []
    lista = []
    while True:
        temp = int(input("Informe os números para a lista (ou '0 para sair) -> "))
        if temp == 0:
            break
        elif temp not in lista:
            lista.append (temp)
            listaF.append (temp)
        else:
            listaF.append (temp)

    print(listaF)
    print(lista)

main()