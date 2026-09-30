#Exercício 04: Cadastro Continuo de Nomes (Laço While e Modos "a")
#Crie um programa a com um laço while que peça para o usuário digitar nomes de pessoas.
#Trate cada nome com os métodos .strip() e .title().
#O programa deve parar de pedir nomes quando o usuário digitar a palavra "Sair".
#A cada nome válido digitado, abra o arquivo "cadastro_nomes.txt" no modo "a" e salve o nome seguido de \n.
#Ao finalizar o laço, exiba: "Cadastro finalizado e salvo no arquivo!".

while True:
    nomes = input("Digite o nome das pessoas que vc quer anotar: ").strip().title()

    if nomes.strip().lower() == "sair":
        break

    with open("nomes_cadastrados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nomes + "\n")

print("Cadastro salvo na boxta da lista")