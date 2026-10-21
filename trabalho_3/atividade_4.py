import json

json_string = '{"usuario": "dev_python", "nivel": "intermediario", "ativo": true}'

usuario = json.loads(json_string)

if usuario["ativo"]:
    print(f"Bem-vindo, {usuario['usuario']}! Nível: {usuario['nivel']}.")
else:
    print(f"Acesso negado: o usuário {usuario['usuario']} está inativo.")