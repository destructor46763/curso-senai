contador = 0

while contador != 5:
    nota_1 = float(input("digite a primeira nota"))
    nota_2 = float(input("digite a segunda nota"))
    nota_3 = float(input("digite a terceita nota"))

    media = (nota_1 + nota_2 + nota_3) / 3

    if media >= 6:
        print("aprovado")
    
    elif media >= 4 and media <= 5.9:
        print("recuperação")

    else:
        print("reprovado")
    
    contador += 1


