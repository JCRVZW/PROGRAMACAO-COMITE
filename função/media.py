def calcular_media (*num):
    soma = 0
    for n in num:
        soma += n

    return soma / len(num)

def main ():
    media = calcular_media(4,5,6,10)
    print(f"a média é {media}")

main()