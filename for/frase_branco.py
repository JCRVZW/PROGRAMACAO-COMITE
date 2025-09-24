frase = str(input("Digite sua frase -> "))
contador = 0

for letra in frase:
    if letra == " ":
        contador +=1

print (f"A quantidade de espaços é {contador}")