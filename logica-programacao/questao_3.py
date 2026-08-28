# Leia a idade de 10 pessoas. Classifique cada uma como criança, adolescente, adulto ou idoso. Ao final, informe quantas pessoas há em cada grupo.

adulto = []
idoso = []
criança = []
adolescente = []

contador = 0

while contador != 10:
    idade = int(input("Digite a sua idade: "))

    if idade <= 13 and idade >= 0:
        criança.append(idade)

    elif idade > 13 and idade <= 17:
            adolescente.append(idade)

    elif idade > 17 and idade < 60:
            idoso.append(idade)

    else:
            idoso.append(idade)

    contador += 1

print(f"o número de crianças é: {len(criança)} pessoas.")
print(f"o número de adolescente é: {len(adolescente)} pessoas.")
print(f"o número de adultero é: {len(adulto)} pessoas.")
print(f"o número de idoso é: {len(idoso)} pessoas.")

