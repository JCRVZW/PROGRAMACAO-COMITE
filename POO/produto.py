class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

def main():
    nome = input("Informe o nome do produto -> ")
    preco = float(input("Insira o preço do produto -> "))
    meu_produto = produto(nome, preco)
    print(f"{meu_produto.nome} custa R$ {meu_produto.preco:.2f}")
    print("Deseja aplicar um desconto? (S/N)")
    resposta = input().upper()
    if resposta == 'S':
        percentual = float(input("Informe o percentual de desconto -> "))
        meu_produto.desconto(percentual)
        print(f"Novo preço de {meu_produto.nome} após {percentual}% de desconto é R$ {meu_produto.preco:.2f}")
    else:
        print("Nenhum desconto aplicado!")
main()
