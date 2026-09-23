estoque = ["Multímetro", "Protoboard", "Resistor", "Multímetro", "Cabo", "Multímetro", "Protoboard"]
print("=" * 30)

print(estoque)
equipamento_de_pesquisa = input("Qual equipamento você quer utilziar?: ").strip().title()

if equipamento_de_pesquisa in estoque:
    print(f"O item {equipamento_de_pesquisa} aparece {estoque.count (equipamento_de_pesquisa)} vez(es) no estoque.")

else:
    print("não temos esse equipamento no estoque")    



