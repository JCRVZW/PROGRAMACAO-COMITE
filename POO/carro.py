class carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f"ligando o {self.modelo} | Ano {self.ano}")

def main():
    carro1 = carro(input("Digite o modelo do carro -> "), input("Digite o ano do carro -> "))
    carro1.ligar()
main()