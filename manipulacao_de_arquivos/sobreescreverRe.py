def obter_texto():
    texto = input("Informe uma palavra -> ")
    print("Novo texto obtido!")
    return texto

def escrever():
    with open ("new_text.txt", "w") as arquivo:
        arquivo.write (obter_texto())
    print("Novo texto Gravado!")

def main():
    escrever()
main()