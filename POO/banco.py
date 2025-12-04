class conta:
    def __init__(self, saldo):
        self.saldo = int(saldo)

    def depositar(self, valor):
        print(f"\nSaldo anterior | {self.saldo} |")
        self.saldo += valor
        print(f"Saldo atual | {self.saldo} |")

    def sacar(self, valor):
        print(f"\nSaldo anterior | {self.saldo} |")
        self.saldo -= valor
        print(f"Saldo atual | {self.saldo} |")

def main():
    minha_conta  = conta(3000)
    minha_conta.sacar(int(input("Digite o valor a ser sacado -> ")))

    print("\n o saldo atual é -> ", minha_conta.saldo)
    minha_conta.depositar(int(input("Digite o valor a ser depositado -> ")))

main()