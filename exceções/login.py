class SenhaIncorretaError(Exception):
    pass

class SenhaFracaError(Exception):
    pass

def fazer_login(senha_usuario):
    logar = input('\n\nInforme sua senha -> ')

    if logar == senha_usuario:
        print("\n Login efetuado com sucesso!\n\n")
    else:
        print('\nTente novamente!')
        raise SenhaIncorretaError("Senha incorreta!\n\n")
    
def cadastrar_senha():
    print("\nCADASTRO DE SENHA")
    senha_usuario = input('Informe a senha -> ')

    if len (senha_usuario) <10:
        print("\nTente novamente: ")
        raise SenhaFracaError ("Senha deve conter 10 caracteres!\n")
    else:
        print("\n Senha cadastrada com sucesso\n")

        return senha_usuario
    
def menu():
    senha_usuario = '0'
    while True:
        try:
            opcao = int(input(f"1 - Criar senha\n
                              ''