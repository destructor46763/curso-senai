print("\n ----QUESTIONARIO---- ")
nome_do_aluno = input("qual o nome do aluno?: ")
turma_do_aluno = input("qual a turma do aluno?: ")
materia = input("qual a matéria?: ")
professor_atuando_na_materia = input("qual o professor que está atuando na área?: ")

print = ("\n ----NOTA NA MATERIA---- ")
a1 = int(input("qual a primeira nota da materia?: "))
a2 = int(input("qual a segunda nota da materia?: "))
a3 = int(input("qual a terceita nota da materia?: "))

media = (a1 + a2 + a3) /3

print("\n ==== RESULTADO ====")
print("nome:", nome_do_aluno)
print("turma:", turma_do_aluno)
print("materia:", materia)
print("professor:", professor_atuando_na_materia)
print("média:", media)
