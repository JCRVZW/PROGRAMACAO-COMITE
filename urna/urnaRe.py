opcao = -1
encerrar = 1909
encerrar_votacao = 1900
candidatos = []
contagem_votos = {"nulos": 0}

#Menu principal
while opcao != encerrar:
    opcao = input ('O que deseja fazer? \n' 
                        'opção 1: Cadastrar os candidatos  \n' 
                        'opção 2: iniciar votaçao \n' 
                        'opção 3: exibir ganhador \n'
                        'opção 0: Sair \n\n' 
                        'Opção -> ')

#valida se a opção é um número

    if opcao.isdigit():
        opcao = int(opcao)

    #testa para opções da urna
    
        if opcao == 1:
            qtd_cand = int(input('Quantos candidatos deseja cadastrar? '))

        #laço para cadastrar candidato
            for c in range(1, qtd_cand+1):
                candidato = []
                nome = input(f"Nome do candidato {c} -> ")
                numero = int(input(f"Informe o número do candidato {c} -> "))

                #salva candidato
                candidato.append(nome)
                candidato.append(numero)

                #add candidato
                candidatos.append(tuple(candidato))

            print('\n\n')

        elif opcao == 2:
            voto = -1
            #mostrar candidatos
            while voto != encerrar:
                for candidato in candidatos:
                    print(f"candidato {candidato[0]} | Número {candidato[1]}")

                voto = int(input('Vote no número de um candidato -> '))

                cont = 0

                for candidato in candidatos:
                    cont +=1 
                    if voto == candidato[1]:
                        if candidato[0] not in contagem_votos:
                            contagem_votos.update({candidato[0]: 1})
                            break
                        else:
                            contagem_votos[candidato[0]] += 1
                            break
                    else:
                        if cont == len(candidatos):
                            contagem_votos['nulos'] +=1

    elif opcao == 3:
        #remove nulo incorreto da saida de votacao '1900'
        contagem_votos['nulos'] -=1

        #mostra resultados e vencedor
        maior = 0
        vencedor = ''
        for key, value in contagem_votos.items():
            if value > maior:
                maior = value
                vencedor = key
                print(f"{key} | Votos {value}")

            print(f"O vencedor é {vencedor} com {maior} votos")
            


#se a opção digitada nao for numero cai aqui
    else:
        print('\n\nOpção inválida!')