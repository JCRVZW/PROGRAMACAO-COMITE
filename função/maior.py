import random

def maior(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento>maior:
            maior = elemento
    return maior

def main():
    lista = random.randint(1,100) 
    for num in range (15):


        maior_num = maior(lista)
        print(f"Lista original -> {list}")
        print(f"Maior elemento -> {maior_num}")

main()
