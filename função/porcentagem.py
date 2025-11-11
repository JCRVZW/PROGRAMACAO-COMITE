def calcular (valor, porcentagem):
    novo_valor = valor+(valor*(porcentagem/100))
    return novo_valor

def main():
    valor = int(input('Informe o valor -> '))
    porcentagem = int(input('Informe a % -> '))

    novo_valor = calcular(valor, porcentagem)

    print (f"O valor atualizado é -> {novo_valor}!")

main()