class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"{self.nome} está com {self.idade} anos!")

def main():
    nome = input("Digite o nome da pessoa -> ")
    idade = input("Digite a idade da pessoa -> ")
    pessoa = Pessoa(nome, idade)
    pessoa.apresentar()

main()