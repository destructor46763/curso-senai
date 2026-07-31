num1 = float(input("primeira nota: "))
num2 = float(input("quarta nota: "))
num3 = float(input("terceira nota: "))

média = (num1 + num2 + num3) / 3

if média >= 7:
    print(f"você foi aprovado! {média}")

elif média >= 5 and média < 6.9 :
    print(f"você está de recuperação! {média}")    

else :
    print(f"reprovado fi :D {média}")    


