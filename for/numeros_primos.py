qtd_primos = 0

for num in range (1,1000):
    num_vezes_div = 0

    for num2 in range (1, num+1):
        if num % num2 == 0:
            num_vezes_div += 1
    if num_vezes_div == 2:
        print (f"Numero primo {num}")
        qtd_primos += 1
    if qtd_primos == 20:
        break           