carro = {
    "marca": "Fiat",
    "Modelo": "uno",
    "ano": "2015"
}

for chave in carro:
    print (chave) #chave

for car in carro.values():
    print(car) #todos valores

for chave, valor in carro.items():
    print(chave, '->', valor)