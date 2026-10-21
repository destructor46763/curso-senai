import json

def atualizar_preco(id_produto, novo_preco):
    # 1. Abre o arquivo original para leitura ('r')
    try:
        with open('estoque.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Erro: O arquivo 'estoque.json' não foi encontrado.")
        return

    # 2. Percorre a lista para localizar o produto e atualizar o preço
    produto_encontrado = False
    for produto in dados:
        if produto['id'] == id_produto:
            produto['preco'] = novo_preco
            produto_encontrado = True
            break  
            
    # 3. Se o produto existir, salva as alterações de volta no arquivo ('w')
    if produto_encontrado:
        with open('estoque.json', 'w', encoding='utf-8') as arquivo:
            # indent=4 formata o arquivo de maneira legível para humanos
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"Sucesso: Preço do produto ID {id_produto} atualizado para R$ {novo_preco:.2f}.")
    else:
        print(f"Aviso: Produto com ID {id_produto} não foi encontrado no estoque.")
