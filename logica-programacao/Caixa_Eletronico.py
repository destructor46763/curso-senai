print("\n ---CAIXA ELETRONICO---")

saque = float(input("qual o valor que gostaria de fazer o saque?: "))
saldo = float(input(" qual o seu saldo atual?: "))

if saldo >= saque:
    sub = saldo - (saque + 2)
    print(f"seu saque foi concluido, o saldo atual agora é R$ {sub}")

else:
    print("seu saque foi cancelado, razão: saque indiponivel.")