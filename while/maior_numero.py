numero = 1
maior = 0

while numero != 0:
    numero = int(input ("informe um dígito -> "))

    if numero > maior:
     maior = numero
    else:
        maior = maior
    
print (f"o maior numero é {maior}")