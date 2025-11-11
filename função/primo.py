def verificar(numero):
    divisoes = 0
    for n in range(1,numero+1):
        if numero % n == 0:
            divisoes +=1

    if divisoes == 2: 
        return True
    else:
        return False
    
def main():
    numero = int(input("Insira um número -> "))
    resultado = verificar(numero)
    print(f"O numero é primo? {resultado}")

main()