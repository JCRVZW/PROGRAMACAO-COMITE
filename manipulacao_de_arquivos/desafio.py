def log(nome):
    with open(nome, "r") as arquivo:

        log = arquivo.readlines()

        resultados = {
                "INFO": 0,
                "ERROR": 0,
                "WARNING": 0
     }
        
        for linha in log:
            if "INFO" in linha:
                resultados["INFO"] += 1
            elif "ERROR" in linha:
                resultados["ERROR"] += 1
            elif "WARNING" in linha:
                resultados["WARNING"] += 1

    return resultados
def gerar(resultados):
    with open("relatorio.txt", "w") as arquivo:
        arquivo.write(f"Relatório de LOGS\n")
        for chave, valor in resultados.items():
            arquivo.write(f"Existem {valor} ocorrências de log {chave}!\n")

    for chave, valor in resultados.items():
            print (f"Existem {valor} ocorrências de log {chave}!")


def main():
    nome_arquivo = "log_500.txt"
    resultados = log(nome_arquivo)
    gerar(resultados)
main()
    
    