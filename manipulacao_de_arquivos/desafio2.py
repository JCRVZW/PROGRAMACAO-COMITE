def gerar_boletim(aluno):
    with open("boletim.txt", "w") as boletim:
        for chave, valor in aluno.items():
            if type(valor) != float:
                boletim.write (f'{chave} | {valor}\n')
            else:
                boletim.write (f'{chave} | {valor:.2f}\n')

        for chave, valor in aluno.items():
            if type(valor) != float:
                print (f'{chave} | {valor}')
            else:
                print (f'{chave} | {valor:.2f}')

def calcular_boletim(aluno):
    media = ((aluno['nota1'] + aluno['nota2']) + aluno['nota3']) / 3
    status_aluno = ''
    if media >= 6:
        status_aluno = 'Aprovado'
    else:
        status_aluno = 'Reprovado'

    aluno.update({'media': media,
                   'status': status_aluno})
    gerar_boletim(aluno)
    
def obtem_info():
    aluno = {'nome': '',
             'nota1': 0,
             'nota2': 0, 
             'nota3': 0}
             
             
    aluno['nome'] = input("Digite o nome do aluno -> ")
    aluno['nota1'] = float(input("Digite a nota 1 -> "))
    aluno['nota2'] = float(input("Digite a nota 2 -> "))
    aluno['nota3'] = float(input("Digite a nota 3 -> "))
    return aluno

def main():
    aluno = obtem_info()
    calcular_boletim(aluno)


main()