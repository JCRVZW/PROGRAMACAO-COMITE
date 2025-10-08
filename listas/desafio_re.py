numeros = []
for i in range (5):
    num = float(input(f"Informe o {i+1}º número -> "))
    numeros.append (num)


maior = max(numeros)
menor = min(numeros)

media = (sum(numeros)/len(numeros))

print (f"O maior numero é {maior}! O menor numero é {menor}! E a media é {media}!")