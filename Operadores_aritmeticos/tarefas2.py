numero = int(input("Informe um número que mostrará o seu antecessor e sucessor -> "))
sucessor = numero+1
antecessor = numero-1

print (f"o sucessor de {numero} é {sucessor}, e o antecessor é {antecessor}.")

temp_c = float(input("Insira uma temperatura em °C para converter em °F -> "))
temp_f = float(temp_c*9/5)+32
print (f"Em °F, {temp_c} resulta em {temp_f} graus.")

numero_2 = float(input("Diga o primeiro número para mostrar o quociente inteiro e o resto -> "))
numero_2_2 = float(input("Insira o segundo número -> "))
print (f"O quociente é {numero_2 // numero_2_2} e o resto é {numero_2%numero_2_2}")

base = float (input("Forneça um número para saber sua potência -> "))
expoente = float (input("Informe o expoente -> "))
print (f"O resultado de {base} elevado por {expoente} é {base**expoente}.")
