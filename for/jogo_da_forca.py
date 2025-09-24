secreta = input("Informe a palavra secreta -> ")
encontrada = ["-"] * len(secreta)
chute = ''
tentativas = 1

for tentativa in range (tentativas+1):
    chute = input(f"Chute uma letra {encontrada} -> ")

    for t in range (len(secreta)):
        if secreta [t] == chute:
            encontrada [t] = chute
    if "-" not in encontrada:
        print ("Você venceu!")
        break

    print (f"Faltam apenas {tentativas - tentativa} tentativas")

else:
    print (f"Você perdeu! A palavra era {secreta}")            