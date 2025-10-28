opcao = ()
candidatos = []

while (opcao != 0):
    opcao = int(input('O que deseja fazer? \n' \
                        'opção 1: Cadastrar os candidatos  \n' \
                        'opção 2: Começar votação \n' \
                        'opção 3: Exibir resultados \n'\
                        'opção 0: Sair \n\n' \
                        'Opção -> '))
    
    
    if opcao == 1:
        temp = []
        while True:
            nome = input("Informe o nome do candidato -> ")
            voto = int(input("Insira o número de voto do candidato -> "))
            temp.append (nome)
            temp.append (voto)
            candidatos.append (temp)
            continuar = input("Deseja cadastrar outro candidato? s/n -> ")
            if continuar != ("s"):
                break

    elif opcao == 2:
        
        while True:
            for linha in candidatos:
                chave = ''
                for coluna in linha:
                    chave += str(coluna)
                    print(chave)
                    
            break

        
        
        
            
