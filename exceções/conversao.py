def converter(texto):
    try:
        num = float(texto)
        print(f"{type(num)} | {num}")    
        return True

    except ValueError: 
        print("Informação digitada não é um número")
        print("Tente novamente")
        return False

def obter_informacao():
    while True:
        info = input('Informe um número -> ')

        if converter(info):
            break

def main():
    obter_informacao()

main()