estoque = {
    "caderno": 10,
    "apostila": 12,
    "bolsa": 2
}

for chave, valor in estoque.items():
    print(f"Produto -> {chave} | quantidade -> {valor}!")

estoque.update ({"bolsa": 1, "apostila": 5})
print ("Vendas efetuadas!")

print ("Estoque Atualizado!")
for chave, valor in estoque.items():
    print(f"Produto -> {chave} | quantidade -> {valor}!")