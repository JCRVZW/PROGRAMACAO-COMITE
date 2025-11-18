import json
def jason():
 
    dados = {"nome": "Juca", "idade": 17}
    with open("dados.json", "w") as f:
        json.dump(dados, f, indent=4)
print(jason)