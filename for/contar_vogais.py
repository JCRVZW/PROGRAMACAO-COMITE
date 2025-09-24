palavra = input("insira uma palavra: ")
vogais = 0
for letra in palavra:
    if letra == 'a' or letra == 'e' or\
    letra == 'i' or letra == 'o' or letra == 'u':
        vogais += 1

print (f"a palavra {palavra} tem {vogais} vogais")