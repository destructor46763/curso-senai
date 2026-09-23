turma = [7.5, 4.0, 9.2, 5.5, 3.8, 10.0, 6.5, 2.0]
aprovado = []
recuperação = []

for aluno in turma:
    if aluno > 6:
        aprovados.append(aluno)

    elif aluno < 6:
        reprovados.append(aluno)

print("a media da turma é: ", sum(turma))
print("o numero de alunos reprovados é: ", len(turma))
print("o numero de alunos aprovados é: ", len(turma))