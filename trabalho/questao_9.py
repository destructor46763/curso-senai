contador = 0
notas = []
total = 0

while contador != 5:
    valor = float(input("Quanto de nota você gostaria de colocar ao nosso restaurante? de 1 a 5: "))
    if valor >= 1 and valor <= 5:
        notas.append(valor)
    
        contador += 1
    else:
        print("está nota esta invalida.")

for nota in notas:
    total += nota

print(f"A média do nosso restaurante é: {total / 5}")

