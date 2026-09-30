#Exercício 05: Exportador de Notas e Média (Misturando Listas e Arquivos)
#Dada a lista com as notas de um aluno: notas = [7.5, 8.0, 6.0, 9.5].
#Calcule a média aritmética das notas utilizando sum() e len().
#Abra um arquivo chamado "boletim.txt" no modo "w" com encoding="utf-8".
#Escreva todas as notas separadas por vírgula em uma linha.
#Na linha seguinte, escreva o resultado da média no formato: "Média Final: [Media]". 

notas = [7.5, 8.0, 6.0, 9.5]
media = sum(notas) / len(notas)


with open("boletim.txt", "w", encoding="utf-8") as arquivo:
    notas_em_texto = ", ".join(str(nota) for nota in notas)
    
    arquivo.write(notas_em_texto + "\n")
    
    arquivo.write(f"Média Final: {media:.2f}\n")

print("Boletim exportado com sucesso! porra")

