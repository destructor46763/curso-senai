def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

imc = calcular_imc(77, 180)

def classificar_imc(imc):
    if imc <= 10:
        print("Tá muito magrinho")
    elif imc > 10 and imc <= 18:
        print("Parabéns, você está na media")
    elif imc > 18 and imc < 24:
        print("ParabénS, você está gordo")
    else:
        print("parabéns, você é obeso")

classificar_imc()