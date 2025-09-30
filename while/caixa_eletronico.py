saldo = 5000
valor_saque = 1

print (f"seu saldo é {saldo}")

while valor_saque != 0:
    valor_saque = float(input("informe o valor do saque -> "))
    saldo -= valor_saque
    print (f"o valor restante é {saldo}")