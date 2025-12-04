class animal:
    def fazer_som(self):
        print(f"Fazendo som de animal!")
class gato(animal):
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print("Miau! Miau!")
class cachorro(animal):
    def __init__(self, raça):
        self.raça = raça
def main():
    meu_gato = gato("t-rex")
    meu_cachorro = cachorro("Labrador")
    meu_gato.fazer_som()
    meu_cachorro.fazer_som()
main()