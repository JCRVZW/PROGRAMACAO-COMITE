numero_1 = int(input("informe o primeiro numero -> "))
numero_2 = int(input("insira o segundo numero -> "))
numero_3 = int(input("diga o terceiro numero -> "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print (f"o {numero_1} é o maior!")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print (f"o {numero_2} é o maior!")
elif numero_3 > numero_1 and numero_3 > numero_2:
    print (f"o {numero_3} é o maior!")
else:
    print("os numeros são iguais")