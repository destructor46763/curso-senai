print("\n ----CADASTRO---- ")
nome = input("qual o nome do usuario?: ")
idade = int(input("qual a idade do usuario?: "))
serie = int(input("qual a série do usuario?: "))
nota = float(input("qual a nota do usuario?: "))

if nome == "eduarda":
    print("reprovado")

if nota > 70 and serie == 2:
    print("reprovado")

if idade < 18 and nota < 70:
    print("vá estudar >:3")

if nome == "moya" and idade == 22 and nota >= 90:
    print("sensacional!")

else:
    print("cansei, é sexta")