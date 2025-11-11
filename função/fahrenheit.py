def graus (a,b,c):
    return a*b+c

def main():
    a = float(input("informe o grau em celsius -> "))
    resultado = graus (a,1.8,32)
    print (f"{a}° graus em Fahrenheit é {resultado}° graus!")

main()    