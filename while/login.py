usuario = "adm" 
senha = "123"
tentativas = 3


while tentativas > 0:
    if input("Informe o usuário -> ") == usuario:
        if input("Informe a senha -> ") == senha:
            print (f"Bem vindo {usuario}!")
            break
        else:
            print ("Senha incorreta, tente novamente")

            tentativas += 1

            print (f"{tentativas} tentativas restantes!")
    else:
        print ("usuario incorreto, tente novamente!")

        tentativas -= 1

        print (f"{tentativas} tentativas restantes!")        
