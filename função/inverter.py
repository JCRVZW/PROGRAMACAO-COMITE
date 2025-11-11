def main ():
    inversa = ""
    palavra = str(input("Insira uma palavra -> "))
    for letra in palavra:
        inversa = letra + inversa
    print(inversa)

main()
