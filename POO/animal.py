class animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self, som):
        print(f"{self.nome}, o/a {self.especie}, faz o som -> {som}")
def main():
    nome = input("Informe o nome do animal -> ")
    especie = input("Informe a espécie do animal -> ")
    meu_animal = animal(nome, especie)
    som = input("Informe o som que o animal faz -> ")
    meu_animal.fazer_som(som)
main()