lista = ["Romeu", "Julieta", "Abracadabra", "Pinoia"]

dicionario = {}

for palavra in lista:
    chave = f"qtd palavras - {len(palavra)}"
    valor = len(palavra)
    dicionario.update ({chave: valor})

for chave, valor in dicionario.items():
    print(f'{chave} | {valor}')