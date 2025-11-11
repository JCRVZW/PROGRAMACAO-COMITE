def contar (texto):
    vogais = "a", "e", "i", "o", "u"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador +=1

    return contador

def main ():
    qtd_vogais = contar(input("digite o texto -> "))
    print(f"o texto tem {qtd_vogais} vogais!")

main()