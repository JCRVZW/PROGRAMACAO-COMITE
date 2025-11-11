def fato ():
    num = int(input("Informe um número para saber seu fatorial -> "))
    fatorial = 1
    for numero in range (1, num+1):
        fatorial *= numero 
    print (fatorial)

def main ():
    fato()
main()