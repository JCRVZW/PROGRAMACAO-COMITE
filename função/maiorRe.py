import random

def maior(lista):
     maior = max(lista)

def main():
    lista = [random.randint(1,100) for num in range (15)]
    
    print(f"Lista original -> {lista}")
    maior = max(lista)
    print(f"Maior elemento -> {maior}")

main()