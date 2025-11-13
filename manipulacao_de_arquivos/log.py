from datetime import datetime

def log():
    with open ('log.txt', 'w') as arquivo:
        for i in range(3):
            agora = datetime.now()
            arquivo.write(f'{agora} LOG {i+1}\n')

        print("LOG gerado com sucesso!")

def main():
    log()
main()