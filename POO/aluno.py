class aluno:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
    def media(self):
        return (self.nota1 + self.nota2) / 2
    
def main():
    nota1 = float(input("Informe a primeira nota do aluno -> "))
    nota2 = float(input("Informe a segunda nota do aluno -> "))
    meu_aluno = aluno(nota1, nota2)
    print(f"A média do aluno é -> {meu_aluno.media():.2f}!")
main()