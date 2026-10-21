import json

produto = {
    "nome": "Notebook Gamer XPro",
    "preco": 4599.90,
    "quantidade_estoque": 12,
    "categorias": ["informática", "notebooks", "gamer"]
}

with open("produto.json", "w", encoding="utf-8") as arquivo:
    json.dump(produto, arquivo, ensure_ascii=False, indent=4)

print("Arquivo produto.json criado com sucesso!")