def log(nome):
    with open(nome, "r") as arquivo:

        log = arquivo.readlines()

        resultados = ("INFO": 0,
                       "ERROR": 0,
                         "WARNING": 0)
        
        for linha in log:
            if "INFO" in linha:
                resultados["INFO"] += 1
            elif "ERROR" in linha:
                resultados["ERROR"] += 1
            elif "WARNING" in linha:
                resultados["WARNING"] += 1

    return resultados
def gerar():
        with open("relatorio.txt", "w") as arquivo:
            arquivo.write(f"Relatório de LOGS\n")
            for chave, valor in resultados.items():
                arquivo.write(f"Existem {chave} ocorrências de log {valor}!\n")

        print("Relatório criado!")
        for chave, valor in resultados.items():
            arquivo.write(f"Existem {chave} ocorrências de log {valor}!\n")

def main():
    nome_arquivo = "log_5000.txt"
    resultados = log(nome_arquivo)
    gerar(resultados)
    
    