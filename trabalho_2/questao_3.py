# Exercício 03: Gerador de Lista de Compras (.writelines())
# Crie uma lista vazia chamada compras.
# Utilize um laço for para solicitar que o usuário digite 5 itens de supermercado, adicionando cada item à lista compras já com o caractere \n ao final.
# Abra um arquivo chamado "lista_compras.txt" no modo "w".
# Escreva todos os itens de uma vez só utilizando o método .writelines(compras).
# Exiba na tela: "Lista de compras gerada com sucesso!".

compras = []
contador = 0

while contador != 5:
    item = input(f"Digite o {contador}° item de supermercado: ")
    compras.append(item + "\n")

    contador += 1

with open("lista_compras.txt", "w") as arquivo:
    arquivo.writelines(compras)

print("sua lista de compras foi gerada com sucesso!")