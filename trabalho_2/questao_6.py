#Exercício 06: Registro de Log de Eventos (Formatação de Strings)
#Crie um programa que simule um sistema de login simples.
#Solicite o nome do usuário e o status do acesso (ex: "Sucesso" ou "Falha").
#Abra o arquivo "sistema_logs.txt" no modo "a" com encoding="utf-8".
#Escreva uma linha de log formatada da seguinte forma: "[LOG] - Usuario: [Nome] | Status: [Status]\n".
#Exiba a mensagem: "Evento registrado no log do sistema.".

nome_usuario = input("Digite o nome do usuário: ").strip()
status_acesso = input('Digite o status do acesso "Sucesso" ou "Falha"): ').strip().title()

with open("sistema_logs.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"[LOG] - Usuario: {nome_usuario} | Status: {status_acesso}\n")

print("Evento registrado no log do sistema.")
