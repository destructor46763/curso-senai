import json

with open("produto.json", "r", encoding="utf-8") as arquivo:
    produto = json.load(arquivo)

categorias = ", ".join(produto["categorias"])

print(
    f"Produto: {produto['nome']} | "
    f"Preço: R$ {produto['preco']:.2f} | "
    f"Estoque: {produto['quantidade_estoque']} unidades"
)
print(f"Categorias: {categorias}")