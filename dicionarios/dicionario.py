carro = {
    "marca": "Fiat",
    "Modelo": "uno",
    "ano": "2015"
}
print (carro["marca"])

carro["cor"] = "cinza"
carro.update ({"vidro": "manual", "roda": "quatro"})

print(carro["cor"])
print(carro["vidro"])
print(carro["roda"])