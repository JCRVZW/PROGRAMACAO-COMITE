carro = {
    "marca": "Fiat",
    "modelo": "uno",
    "ano": 2015
}
#carro['ano'] = 2020 #atualizar valor do ano
carro.update({"ano": 2020})
print (carro["ano"])

carro.pop ('modelo') #remover o item "modelo"
print (carro.get('modelo'))
