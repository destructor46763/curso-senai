valor = int(input("qual sua nota: "))

if valor <= 0 or valor % 10 != 0:
    print("VALOR INVALIDO = o seu valor tem que ser multiplicado por 10")

else: 
    valor_restante = valor

notas_de_100 = valor_restante // 100 # as duas (//) barras servem para uma divisão inteira, sendo assim, os numeros depois da virgula não aparecem
valor_restante %= 100

notas_de_50 = valor_restante // 50
valor_restante %= 50

notas_de_20 = valor_restante // 20 
valor_restante %= 20

notas_de_10 = valor_restante // 10

print(f"\nSeu saque de R$ {valor} foi realizado com sucesso!")
print(f"\nNotas de 100: --{notas_de_100}--")
print(f"\nNotas de 50: --{notas_de_50}--")
print(f"\nNotas de 20: --{notas_de_20}--")
print(f"\nNotas de 10: --{notas_de_10}--")

