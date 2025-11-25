def converter(texto):
    try:
        num = float(texto)
        print(f'{type(num)} | {num}')
        print(num * "a")
        return True
    except ValueError:
        print ("O valor não é um número!")
        print ("tente novamente!")
        return False
    except TypeError:
        print("Você está tentando usar um tipo inválido")
        print("Tente novamente")
        return False
    
def obter_informacao():
    while True:
        info = input("Informe um Número -> ")
        if converter(info):
            break

def main():
    obter_informacao()
main()