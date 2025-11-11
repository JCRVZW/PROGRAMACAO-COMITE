def boletim ():
    name = str(input("Informe o nome do aluno -> "))
nome = str(input("Informe o nome do aluno -> "))
n1 = float(input("Insira a nota do primeiro trimestre -> "))
n2 = float(input("Insira a nota do segundo trimestre -> "))
n3 = float(input("Insira a nota do terceiro trimestre -> "))
media = (n1+n2+n3)/3
if media >= 7:
    situacao = "Aprovado"
elif media > 5.9:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
    

aluno = {"nome": nome, "média": media, "situação": situacao}

print(aluno)

def main():
    boletim()
main()