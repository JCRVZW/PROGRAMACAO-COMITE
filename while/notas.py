nota = 0
soma = 0
quant = 0

while nota >= 0:
    nota = int(input ("informe uma nota -> "))
    soma += nota
    quant += 1

print (f"A media das notas é -> {soma / quant}")
