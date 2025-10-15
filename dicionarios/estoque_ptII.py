estoque = {
    "caderno": 10,
    "apostila": 12,
    "bolsa": 2
}

estoque ["mochila"] = 3
del estoque["apostila"]

print (estoque)

estoque.clear()

print (f"estoque vazio {estoque}")
