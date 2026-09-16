senha_correta = 153
contador = 0

while True:
    senha = int(input("Digite o seu palpite para acertar a senha: "))

    if senha_correta > senha:
        print("Tá mais baixo que o numero que era pra ser :P")

    elif senha_correta < senha:
        print("Tá mais alto que o numero que era pra ser o viado")

    elif senha_correta == senha:
        print(f"opa, parece que você acertou agora, seu total de tentativas foram {contador}")
        break

    contador += 1