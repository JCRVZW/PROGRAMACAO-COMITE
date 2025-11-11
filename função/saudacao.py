def saudacao (nome, idade):
    return f"olá {nome}, parabéns pelos seus {idade} anos!"

def main():
    nome = input('Informe seu nome -> ')
    idade = int(input("Insira sua idade -> "))

    boas = saudacao(nome,idade)
    print(boas)

main()