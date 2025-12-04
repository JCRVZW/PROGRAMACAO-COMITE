class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

def main():
    largura = float(input("Informe a largura do retângulo -> "))
    altura = float(input("Informe a altura do retângulo -> "))
    meu_retangulo = retangulo(largura, altura)
    print(f"A área do retângulo é -> {meu_retangulo.area():.2f}!")
main()