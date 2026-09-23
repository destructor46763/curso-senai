nomes = []
contador = 0

while contador != 5:
    nome = input("digite por favor o nome que deseja adicionar a lista: ").strip().title()

    if nome in nomes:
        print("esse nome já existe na lista.")

    else:
        nomes.append(nome)
        print("o nome foi adicionado com sucesso")

        contador += 1