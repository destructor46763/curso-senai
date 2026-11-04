import sqlite3

conexao = sqlite3.connect("pastinha.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS documentos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               preco REAL NOT NULL,
               estoque INTEGER NOT NULL
               )
               ''')

print("\n CADASTRO: ")

dados = {
    "nome": input("Digite o nome do produto: "),
    "preco": float(input("Digite o preço do produto: ")),
    "estoque": int(input("Digite o numero de itens no estoque: "))
}

cursor.execute('''INSERT INTO documentos (nome,preco,estoque) VALUES (?,?,?)''', (dados["nome"], dados["preco"], dados["estoque"]))

conexao.commit()

print("\n VISUALIZAR PRODUTOS: ")

cursor.execute('''SELECT * FROM documentos''')
produtos = cursor.fetchall()

for produto in produtos:
    print(f" ID:{produto[0]} NOME:{produto[1]} PREÇO:{produto[2]} ESTOQUE:{produto[3]}")

print("\n PREÇO MAXIMO: ")

preco = float(input("qual o preço que você pagaria em um produto: "))

if preco >= 0:  
    for produto in produtos:
        if produto[2] <= preco:
            print(f" ID:{produto[0]} NOME:{produto[1]} PREÇO:{produto[2]} ESTOQUE:{produto[3]}")


        
