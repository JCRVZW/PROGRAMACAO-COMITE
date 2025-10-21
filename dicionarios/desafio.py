alunos = {}
while True:
     nome = input ("informe o nome do aluno -> ")
     idade = int(input("Insira a idade do aluno -> "))
     nota = float(input("diga a nota do aluno -> "))

     alunos.update ({"nome": nome,"idade": idade, "nota": nota})
    
     continuar = input("deseja cadastrar outro aluno? (s/n) -> ")
     if continuar != "s":
        break
     
print(alunos)