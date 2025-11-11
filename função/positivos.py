def contar():
    contador = 0
    lista = []
    while True:
        temp = int(input("Informe os números para a lista (ou '0' para sair) -> "))
        if temp > 0:
            contador +=1
            lista.append(temp)
        elif temp < 0:
            lista.append(temp)
        else:
            break
    print(f"Lista original -> {lista}")
    print(f"Existem {contador} números postivos!")

def main():
    contar()
main()