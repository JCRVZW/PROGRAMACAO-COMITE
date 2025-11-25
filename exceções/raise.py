def verifica_idade(idade):
    if idade <0:
        raise ValueError ("A idade não pode ser negativa")
    print(f"Idade correta {idade}")
    return True

def obtem_idade():
    return int(input("Informe sua idade -> "))

def main():
    while True:
        try:
            idade = obtem_idade()
            if 