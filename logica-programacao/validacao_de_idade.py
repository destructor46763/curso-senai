idade = int(input("digite a sua idade"))
while True:
    if idade > 0 and idade < 13:
        print("você =e criança.")
        idade = int(input("digite sua idade: "))

        elif idade >= 13 and idade < 18:
            print("você é adolescente")
            idade = int(input("digite sua idade: "))
        
        elif idade >= 18 and idade < 60:
            print(você é adultero)
            idade = int(input("digite sua idade: "))

        elif idade >= 60 and idade < 120:
            print(você é velho dms mano)
            idade = int(input("digite sua idade: "))

        else:
            print("morreu ainda nn?")
            idade = int(input("digite sua idade: "))
            


