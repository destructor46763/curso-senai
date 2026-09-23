notas_turma = [5.5, 9.0, 2.5, 10.0, 7.2, 4.0]

notas_turma.sort()
print("Notas da turma em ordem crescente: ", notas_turma)

notas_turma.sort(reverse=True)
print("Notas da turma em ordem crescente: ", notas_turma)

menor_nota = min(notas_turma)
maior_nota = max(notas_turma)

print(f"A menor nota da turma é: {menor_nota}")
print(f"A maior nota da turma é: {maior_nota}")