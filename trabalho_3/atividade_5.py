import json

# 1. Abre o arquivo e lê a lista existente
with open("clientes.json", "r", encoding="utf-8") as arquivo:
    clientes = json.load(arquivo)

# 2. Pede os dados do novo cliente
print("Cadastro de novo cliente")
nome = input("Nome: ")
email = input("E-mail: ")
idade = int(input("Idade: "))

# 3. Adiciona o novo cliente à lista
novo_cliente = {"nome": nome, "email": email, "idade": idade}
clientes.append(novo_cliente)

# 4. Salva a lista atualizada no arquivo
with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, ensure_ascii=False, indent=4)

print(f"Cliente {nome} adicionado. Total de clientes: {len(clientes)}")