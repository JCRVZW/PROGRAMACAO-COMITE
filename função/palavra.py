def contagem_caracteres(palavras):
    return len(palavras)

def main():
    tamanho = contagem_caracteres(input("Digite uma palavra -> "))
    print(f"A palavra tem {tamanho} caracteres!")

main()