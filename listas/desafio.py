num1 = float(input("Informe um numero -> "))
num2 = float(input("Informe um numero -> "))
num3 = float(input("Informe um numero -> "))
num4 = float(input("Informe um numero -> "))
num5 = float(input("Informe um numero -> "))

lista = [num1, num2, num3, num4, num5]

maior = max(lista)
menor = min(lista)

media = ((num1+num2+num3+num4+num5)/5)

print (f"O maior numero é {maior}! o menor numero é {menor}! e a media é {media}!")