#Controle de estoque
   #Cadastre 5 produtos com nome e quantidade. Informe se o estoque está:
   #- Zerado;
   #- Baixo (1 a 10 unidades);
   #- Regular (11 a 50);
   #- Alto (acima de 50).
   #- Mostre quantos produtos estão com estoque baixo ou zerado.

contador = 0
baixo = []
zerado = []
normal = []
muito = []

while contador != 5:
    produto = int(input("quantas unidades restantes: "))
    nome_produto = input("digite o nome do produto: ")

    if produto > 0 and produto == 0:
        print("seu estoque está zerado")
        zerado.append(produto) 
        baixo.append(nome_produto)

    elif produto >= 1 and produto <= 10:
        print("tem que restocar isso ai")
        baixo.append(produto)
        baixo.append(nome_produto)

    elif produto >= 11 and produto <= 50:
        print("o nivel está na normalidade pae")
        normal.append(produto)
        normal.append(nome_produto)

    else:
        print("ta sobrando fi")
        muito.append(produto)
        muito.append(nome_produto)

    contador += 1

print(f"os produtos que estão zerados são: {zerado} e são um total de {len(zerado)} produtos. ")
print("-" * 20)
print(f"os produtos precisam ser retocados são: {baixo} e são um total de {len(baixo)} produtos. ")
print("-" * 20)
print(f"os produtos que estão na medida do normal são: {normal} e são um total de {len(normal)} produtos. ")
print("-" * 20)
print(f"os produtos que estão sobrando são: {muito} e são um total de {len(normal)} produtos. ")

