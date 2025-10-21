alunos = {}
opcao = -1

while (opcao != 0):
    opcao = int(input('O que deseja fazer? \n' \
                        'opção 1: Cadastrar aluno \n' \
                        'opçâo 2: Exibir média \n' \
                        'opção 3: Exibir aluno com maior nota\n' \
                        'opção 0: Sair \n\n' \
                        'Opção -> '))
    
    if opcao == 1:
        key_aluno = len(alunos) + 1
        values_alunos = {}

        nome_aluno = input('Informe o nome do aluno -> ')
        idade_aluno = int(input("Informe a idade do aluno -> "))
        nota_aluno = float(input('Informe a nota do aluno -> '))
        values_alunos.update ({key_aluno: values_alunos})
        print()
    elif opcao == 2:
        soma_notas = 0

        for aluno in alunos.values():
            soma_notas += aluno["nota"]

        print(f"A média das notas é {soma_notas / len(alunos)}\n")

    elif opcao == 3:
        maior = 0 
        id = 0

        for id, aluno in alunos.items():
            if aluno ['nota'] > maior:
                maior = aluno ["nota"]
                id_aluno = id

        print(
            f"O aluno com a maior nota é {alunos[id_aluno]["nome"]} | nota {maior}")
        
    else:
        print ("\n Opção inválida \n")