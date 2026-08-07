senha = 34222074
senha_correta = int(input("digite a sua senha: "))

while True:
    if senha_correta == senha:
        print("senha correta")
        break

    else:
        print("senha incorreta")
        digite = input("digite a sua senha: ")

