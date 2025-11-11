def calculadora ():
    while True: 
        n1 = float(input("insira o primeiro número -> "))
        n2 = float(input("insira o segundo número -> "))
        op = input("Informe a operaçâo (digite 'sair' para sair) -> ")

        if op == "sair":
            break
        elif op == "+":
            resultado = n1 + n2
            print (f"O resultado é {resultado}!")
        elif op == "-":
            resultado = n1 - n2
            print(f"O resultado é {resultado}!")
        elif op == "*":
            resultado = n1 * n2
            print(f"O resultado é {resultado}!")
        elif op == "/":
            if n2 == 0:
                print("ERRO, divisão por zero!")
                continue
            resultado = n1 / n2
            print(f"O resultado é {resultado}!")
        else:
            print("Operação inválida!")
        


def main():
    calculadora()
main()
            
