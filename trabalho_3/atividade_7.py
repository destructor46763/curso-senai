import json

def deletar_tarefa(id_tarefa):
    # 1. Abre o arquivo e lê a lista de tarefas
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    
    # 2. Procura a tarefa pelo ID dentro da lista
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefas.remove(tarefa) # Remove a tarefa se achar o ID
            break 
            
    # 3. Salva a lista atualizada de volta no arquivo
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
        
    print("Processo concluído! Verifique o arquivo.")