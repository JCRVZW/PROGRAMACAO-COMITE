import os
def apagar():
    os.remove("dados.txt")
    print("arquivo apagado com sucesso!")
def main():
    apagar()
main()
