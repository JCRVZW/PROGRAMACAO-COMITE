lista = ["Romeu", "Julieta", "Abracadabra", "Pinoia"]

dicionario = {}

for palavra in lista:
    if f'qtd palavras - {len(palavra)}'not in dicionario.keys():
        chave = f"qtd palavras - {len(palavra)}"
        valor = 1
        dicionario.update({chave: valor})
    else:
        dicionario [f"qtd palavras - {len(palavra)}"] +=1

for chave, valor in dicionario.items():
    print(f'{chave} | {valor}')