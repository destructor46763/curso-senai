import json
import os

NOME_ARQUIVO = "configuracoes.json"

# Configurações padrão caso o arquivo precise ser criado ou resetado
CONFIG_PADRAO = {
    "tema": "escuro",
    "notificacoes": True
}

try:
    with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
        configuracoes = json.load(arquivo)
        
    print("Configurações carregadas com sucesso:")
    print(json.dumps(configuracoes, indent=4, ensure_ascii=False))

except (FileNotFoundError, json.JSONDecodeError) as erro:
    if isinstance(erro, FileNotFoundError):
        print(f"O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
    else:
        print(f"O arquivo '{NOME_ARQUIVO}' estava vazio ou corrompido.")
        
    print("Criando um novo arquivo com as configurações padrão...")
    
    # Cria/Sobrescreve o arquivo com o dicionário padrão
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(CONFIG_PADRAO, arquivo, indent=4, ensure_ascii=False)
        
    print("Arquivo configurado com sucesso!")
