
total_iniciantes = 0
total_intermediarios = 0
total_avancados = 0

maior_pontuacao = -1
nome_vencedor = ""

for i in range(1, 7):
    print(f"--- Jogador {i} ---")
    nome = input("Digite o nome do jogador: ")
    pontuacao = int(input("Digite a pontuação do jogador: "))
    
    if pontuacao <= 20:
        nivel = "Iniciante"
        total_iniciantes += 1
    elif pontuacao <= 50:
        nivel = "Intermediário"
        total_intermediarios += 1
    else:
        nivel = "Avançado"
        total_avancados += 1
        
    if pontuacao > maior_pontuacao:
        maior_pontuacao = pontuacao
        nome_vencedor = nome

print("\n====== RESULTADO FINAL ======")
print(f"O jogador com a maior pontuação foi {nome_vencedor} com {maior_pontuacao} pontos.")
print("\nQuantidade de jogadores por nível:")
print(f"- Iniciante: {total_iniciantes}")
print(f"- Intermediário: {total_intermediarios}")
print(f"- Avançado: {total_avancados}")