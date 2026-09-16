senha = 67
usuario = "drogas"

contador = 0

while contador != 3:
    nome = input("digite o nome do login: ")
    sua_senha = int(input("digite sua senha numérica:" ))

    if nome != usuario and sua_senha != senha:
        print("caia fora! Sistema de segurança contra drogados ativado.")

    else:
        print("bem vindo, maconheiro! ")

    contador += 1 