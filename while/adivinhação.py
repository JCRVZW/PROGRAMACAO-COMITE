import random
numero = random.randint (1,100)
tentativas = 0


while True:

    chute = int(input("Informe um dígito entre 1 e 100 -> "))
    tentativas += 1

    if chute > numero:
        print ("O chute foi maior que o numero!")
        
    elif chute < numero:
        print ("o chute foi menor que o numero!")
    else: 
        print (f"{tentativas} TENTATIVAS! ROCK AND ROLL!!!")
        break

